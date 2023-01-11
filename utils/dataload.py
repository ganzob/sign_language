
import numpy as np
from torch.utils.data import Dataset
import torch


class CustomTensorDataset(Dataset):
    """TensorDataset with support of transforms.
    """

    def __init__(self, tensors, transform=None):
        assert all(tensors[0].shape[0] == tensor.shape[0]
                   for tensor in tensors)
        self.tensors = tensors
        self.transform = transform

    def __getitem__(self, index):
        x = torch.from_numpy(self.tensors[index]).type(torch.FloatTensor)
        # if self.transform:
        #    x = self.transform(x)

        #z = torch.from_numpy(np.array(self.tensors[1][index]))
        #z = self.tensors[1][index]
        # print(index)
        z = torch.Tensor([int(index)]).squeeze()
        return x, z  # torch.Tensor(int(index/2))

    def __len__(self):
        return self.tensors.shape[0]


class CustomTensorDatasetTrain(CustomTensorDataset):
    """TensorDataset with support of transforms.
    """

    def __init__(self, tensors, n_class=32, transform=None):
        super().__init__(tensors, transform)
        self.class_arange = np.arange(n_class)
        #self.order = []
        self.order = [int(i/2) for i in range(n_class*2)]
        # print(self.order)
        #self.finished_flag = False
        #self.transform = torch.transfro

    def __getitem__(self, index):
        #x = self.tensors[index]
        # if self.transform:
        #    x = self.transform(x)

        #print('index_train:', index)
        # print('index_train:',self.order[index])
        x = torch.from_numpy(self.tensors[self.order[index]]).type(
            torch.FloatTensor)
        #x = torch.Tensor([self.tensors[self.order[index]]]).type(torch.FloatTensor)
        z = torch.Tensor([self.order[index]]).type(torch.int64).squeeze()

        return x, z

    def __len__(self):
        return self.tensors.shape[0]

    def shuffle(self):
        np.random.shuffle(self.class_arange)
        self.order = []
        for i in self.class_arange:
            self.order = self.order + [i, i]
