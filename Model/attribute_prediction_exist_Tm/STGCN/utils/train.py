from torch.autograd import Variable
import torch
import numpy as np
import random

def train(epoch, dataloader, net, criterion, optimizer, opt):
    train_loss = 0
    net.train()
    for i, (sample_idx, annotation, adj_matrix, label, mask) in enumerate(dataloader, 0):
        net.zero_grad()
        padding = torch.zeros(opt.batchSize, opt.n_node, opt.L, opt.state_dim - opt.annotation_dim).double()
        init_input = torch.cat((annotation, padding), 3)

        if opt.cuda:
            adj_matrix      = adj_matrix.cuda()
            annotation      = annotation.cuda()
            init_input      = init_input.cuda()
            label = label.cuda()
            mask = mask.cuda()

        adj_matrix      = Variable(adj_matrix)
        annotation      = Variable(annotation)
        init_input      = Variable(init_input)
        target = Variable(label)
        mask = Variable(mask)

        output = net(init_input, annotation, adj_matrix)

        output_ = []
        target_ = []
        mask_batch, mask_node, mask_attribute = np.where(mask==1)
        for idx in range(len(mask_batch)):
            output_.append(output[mask_batch[idx], mask_node[idx]])
            target_.append(target[mask_batch[idx], mask_node[idx], mask_attribute[idx]])
        output = torch.stack(output_)
        target = torch.stack(target_)

        loss = criterion(output, target)

        loss.backward()
        optimizer.step()

        train_loss += loss.item()

        if i % int(len(dataloader) / 10 + 1) == 0 and opt.verbal:
            print('[%d/%d][%d/%d] Loss: %.4f' % (epoch, opt.niter, i, len(dataloader), loss.item()))

    train_loss /= (len(dataloader.dataset) / opt.batchSize)
    print('Train set: Average loss: {:.4f}'.format(train_loss))

    return train_loss
