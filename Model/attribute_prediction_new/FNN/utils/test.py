from torch.autograd import Variable
import copy
import torch
import numpy as np
import os

os.environ['KMP_DUPLICATE_LIB_OK']='True'

def Matching(n_list_tup, t_list_tup, n, t):
    pair_list = []
    decided_n = set()
    decided_t = set()
    while True:
        for idx in range(len(n)):
            matched_n, matched_t = n[idx], t[idx]
            if matched_n in decided_n or matched_t in decided_t:
                continue
            pair_list.append((n_list_tup[matched_n][0], t_list_tup[matched_t][0]))
            decided_n.add(matched_n)
            decided_t.add(matched_t)
            if len(decided_n) == len(n_list_tup):
                break
            if len(decided_t) == len(t_list_tup):
                decided_t = set()
                break
        if len(decided_n) == len(n_list_tup):
            break
    return pair_list

def BipartiteMatching(new_vec_dic, teacher_vec_dic):
    eps = 0.000001 # zero-division errorの回避用
    # sort済みのタプルのリスト[(node_id, vector)]
    n_list_tup = sorted(new_vec_dic.items(), key=lambda x: x[0])
    t_list_tup = sorted(teacher_vec_dic.items(), key=lambda x: x[0])
    # 二部グラフ全てのsimilarityを計算
    N = np.array([n_v for n, n_v in n_list_tup])
    T = np.array([t_v for t, t_v in t_list_tup])
    normN = np.sqrt(np.sum(N * N, axis=1)) + eps
    normT = np.sqrt(np.sum(T * T, axis=1)) + eps
    similarity_matrix = np.dot(N / normN.reshape(-1, 1), (T / normT.reshape(-1, 1)).T)
    # similarityのsort
    n, t = np.unravel_index(np.argsort(-similarity_matrix.reshape(-1)), similarity_matrix.shape)
    # Greedy Matching
    node_pair_list = Matching(copy.copy(n_list_tup), copy.copy(t_list_tup), n.tolist(), t.tolist())
    return node_pair_list, similarity_matrix

def test(dataloader, net, criterion, opt):
    test_loss = 0
    net.eval()
    for i, (sample_idx, new, teacher, new_num, teacher_num, teacher_idx) in enumerate(dataloader, 0):
        new = Variable(new)
        teacher = Variable(teacher)
        new = net(new)

        loss = 0
        for batch in range(opt.batchSize):
            new_vec_dic = {i: new[batch][i].tolist() for i in range(new_num[batch])}
            teacher_vec_dic = {i: teacher[batch][i].tolist() for i in range(teacher_num[batch])}
            node_pair_list, similarity_matrix = BipartiteMatching(new_vec_dic, teacher_vec_dic)

            new_batch = new[batch][:new_num[batch]]
            transformed_teacher = torch.Tensor(new_num[batch], teacher[batch].shape[1])
            for (n_idx, t_idx) in sorted(node_pair_list, key=lambda x: x[0]):
                transformed_teacher[n_idx] = teacher[batch][t_idx]

            gain = criterion(new_batch, transformed_teacher)
            gain_norm = (gain.mean() + 1) / 2
            loss += -1 * gain_norm.log()

        loss /= opt.batchSize
        test_loss += loss.item()

    test_loss /= (len(dataloader.dataset) / opt.batchSize)
    print('Test set: Average loss: {:.4f}'.format(test_loss))

    return test_loss
