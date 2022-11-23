import os
import random
import paddle
import numpy as np
import paddle
from paddle.vision.transforms import ToTensor
from paddle.vision.datasets import MNIST


def train(model, opt, train_loader, valid_loader):
    use_gpu = True
    paddle.device.set_device('gpu:0') if use_gpu else paddle.device.set_device('cpu')
    print('start training.....')
    model.train()
    for epoch in range(EPOCH_NUM):
        for batch_id, data in enumerate(train_loader()):

