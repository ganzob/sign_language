import torch


class ZHO(torch.utils.data.Dataset):

    def __init__(self, dataset_root, use_cache, ):
        super().__init__()
        self.labels = 1  # labels
        self.list_IDs = 1  # list_IDs
        shared_array_base = mp.Array(ctypes.c_float, nb_samples*c*h*w)
        shared_array = np.ctypeslib.as_array(shared_array_base.get_obj())
        shared_array = shared_array.reshape(nb_samples, c, h, w)
        self.shared_array = torch.from_numpy(shared_array)
        self.use_cache = use_cache

    def __len__(self):

        return len(self.list_IDs)

    def __getitem__(self, index):

        X = None
        y = None
        return X, y


class MyDataset(Dataset):
    def __init__(self):
        shared_array_base = mp.Array(ctypes.c_float, nb_samples*c*h*w)
        shared_array = np.ctypeslib.as_array(shared_array_base.get_obj())
        shared_array = shared_array.reshape(nb_samples, c, h, w)
        self.shared_array = torch.from_numpy(shared_array)
        self.use_cache = False

    def set_use_cache(self, use_cache):
        self.use_cache = use_cache

    def __getitem__(self, index):
        if not self.use_cache:
            print('Filling cache for index {}'.format(index))
            # Add your loading logic here
            self.shared_array[index] = torch.randn(c, h, w)
        x = self.shared_array[index]
        return x

    def __len__(self):
        return nb_samples
