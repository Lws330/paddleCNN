import numpy as np
from numpy.linalg import cholesky
import matplotlib.pyplot as plt
mu = np.array([[3, 5]])
Sigma = np.array([[3, 0.5], [1.5, 3]])
R = cholesky(Sigma)
s = np.dot(np.random.randn(1000, 2), R) + mu
# 注意绘制的是散点图，而不是直方图
plt.plot(s[:,0],s[:,1],'+')
plt.show()