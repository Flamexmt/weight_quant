from torch.utils.data import DataLoader, SubsetRandomSampler
import torch
from torchvision import datasets, transforms
import os

def get(batch_size, data_root='/tmp/public_dataset/pytorch', train=True, val=True, subsample=False, indices=None, **kwargs):
    # data_root = os.path.expanduser(os.path.join(data_root, 'mnist-data'))
    data_root='D:\Picdataset\minst'
    kwargs.pop('input_size', None)
    num_workers = kwargs.setdefault('num_workers', 1)
    print("Building MNIST data loader with {} workers".format(num_workers))
    ds = []
    if train:
        if not subsample:
            train_loader = torch.utils.data.DataLoader(
                datasets.MNIST(root=data_root, train=True, download=True,
                               transform=transforms.Compose([
                                   transforms.ToTensor(),
                                   transforms.Normalize((0.1307,), (0.3081,))
                               ])),
                batch_size=batch_size, shuffle=True, **kwargs)
            ds.append(train_loader)
        else:
            train_loader = torch.utils.data.DataLoader(
                datasets.MNIST(root=data_root, train=True, download=True,
                               transform=transforms.Compose([
                                   transforms.ToTensor(),
                                   transforms.Normalize((0.1307,), (0.3081,))
                               ])),
                batch_size=batch_size, sampler=torch.utils.data.SubsetRandomSampler(indices), **kwargs)
            ds.append(train_loader)
    if val:
        test_loader = torch.utils.data.DataLoader(
            datasets.MNIST(root=data_root, train=False, download=True,
                           transform=transforms.Compose([
                                transforms.ToTensor(),
                                transforms.Normalize((0.1307,), (0.3081,))
                            ])),
            batch_size=batch_size, shuffle=True, **kwargs)
        ds.append(test_loader)
    ds = ds[0] if len(ds) == 1 else ds
    return ds

