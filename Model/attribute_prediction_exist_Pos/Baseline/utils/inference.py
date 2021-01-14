from torch.autograd import Variable
import numpy as np
import os
from scipy.sparse import lil_matrix
from scipy.io import mmwrite
os.environ['KMP_DUPLICATE_LIB_OK']='True' # mmwriteでエラーが出るのを回避


def inference(dataloader, opt, OutputDir, Attribute_idx):
    for i, (sample_idx, annotation, adj_matrix, label, mask) in enumerate(dataloader, 0):
        target = Variable(label)
        mask = Variable(mask)
        output = annotation[:, :, -1][:, :, Attribute_idx]
        output = output.argmax(axis=2)[:, :, np.newaxis]

        # 予測結果とラベルを保存
        os.makedirs(OutputDir + "/output", exist_ok=True)
        for batch in range(opt.batchSize):
            p = output.detach().numpy()[batch]
            t = target[batch].numpy()
            m = mask[batch].numpy()
            mmwrite(OutputDir + "/output/pred" + str(sample_idx.numpy()[batch]), lil_matrix(p))
            mmwrite(OutputDir + "/output/true" + str(sample_idx.numpy()[batch]), lil_matrix(t))
            mmwrite(OutputDir + "/output/mask" + str(sample_idx.numpy()[batch]), lil_matrix(m))