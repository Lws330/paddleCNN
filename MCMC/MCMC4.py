import random
import matplotlib.pyplot as plt
from scipy.io.matlab.tests.test_mio import theta
from scipy.stats import norm

from MCMC.MCMC2 import sigma


def norm_dist_prob(theta):
    y = norm.pdf(theta, loc=3, scale=2)
    return y

T = 5000

t = 0
while t < T:
    t = t + 1
    theta_star = norm.rvs(loc=theta[t - 1], scale=sigma, size=1, random_state=None)
    #print theta_star
    alpha = min(1, (norm_dist_prob(theta_star[0]) / norm_dist_prob(theta[t - 1])))

    u = random.uniform(0, 1)
    if u < alpha:
        theta[t] = theta_star[0]
    else:
        theta[t] = theta[t - 1]


plt.scatter(theta, norm.pdf(theta, loc=3, scale=2))
num_bins = 50
plt.hist(theta, num_bins, normed=1, facecolor='red', alpha=0.7)
plt.show()