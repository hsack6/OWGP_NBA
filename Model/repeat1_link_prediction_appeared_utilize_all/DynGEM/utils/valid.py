from torch.autograd import Variable
import torch

def valid(dataloader, net, criterion, opt):
    valid_loss = 0
    net.eval()
    for i, (sample_idx, annotation, adj_matrix, label, mask) in enumerate(dataloader, 0):
        padding = torch.zeros(opt.batchSize, opt.n_node, opt.L, opt.state_dim - opt.annotation_dim).double()
        init_input = torch.cat((annotation, padding), 3)

        if opt.cuda:
            init_input = init_input.cuda()
            label = label.cuda()
            mask = mask.cuda()

        init_input = Variable(init_input)
        target = Variable(label)
        mask = Variable(mask)

        output = net(init_input)
        valid_loss += criterion(output[0<mask], target[0<mask]).item()

    valid_loss /= (len(dataloader.dataset) / opt.batchSize)
    print('Valid set: Average loss: {:.4f}'.format(valid_loss))

    return valid_loss
