import numpy as np
import paddle
from paddle.nn import BatchNorm1D


data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).astype('float32')
bn = BatchNorm1D(num_features=3)
x = paddle.to_tensor(data)
y = bn(x)
print('output of BatchNorm1D Layer: \n {}'.format(y.numpy()))


a = np.array([1, 4, 7])
a_mean = a.mean()
a_std = a.std()
b = (a - a_mean) / a_std
print('std {}, mean {}, \n output {}'.format(a_mean, a_std, b))