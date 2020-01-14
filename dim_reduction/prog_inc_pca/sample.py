from prog_inc_pca import ProgIncPCA

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from prog_inc_pca import ProgIncPCA

# load data
iris = datasets.load_iris()
X = iris.data
group = iris.target
target_names = iris.target_names

# apply PCA
pca = ProgIncPCA(2, 1.0)
pca.progressive_fit(X, latency_limit_in_msec=10)
Y_a = pca.transform(X)
pca.get_loadings()

# plot results
plt.figure()
colors = ['navy', 'turquoise', 'darkorange']
lw = 2
for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(
        Y_a[group[0:len(Y_a)] == i, 0],
        Y_a[group[0:len(Y_a)] == i, 1],
        color=color,
        alpha=.8,
        lw=lw,
        label=target_name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('Progressive PCA result for Iris')

# add one new feature for each data point and apply PCA again
new_feature = np.random.rand(X.shape[0], 1) * X.max() * 0.5
X = np.append(X, new_feature, 1)
pca = ProgIncPCA(2, 1.0)
pca.progressive_fit(X, latency_limit_in_msec=100)
Y_b = pca.transform(X)

# plot results without geometric transformation (a flip somtime happens)
plt.figure()
for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(
        Y_b[group[0:len(Y_b)] == i, 0],
        Y_b[group[0:len(Y_b)] == i, 1],
        color=color,
        alpha=.8,
        lw=lw,
        label=target_name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('After adding new feature (without geom_trans)')

# apply the progressive geometric transformation
Y_bg = ProgIncPCA.geom_trans(Y_a, Y_b)

plt.figure()
for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(
        Y_bg[group[0:len(Y_bg)] == i, 0],
        Y_bg[group[0:len(Y_bg)] == i, 1],
        color=color,
        alpha=.8,
        label=target_name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('After adding new feature (with geom_trans)')
plt.show()
