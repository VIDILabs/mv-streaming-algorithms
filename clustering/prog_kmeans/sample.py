import csv

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from prog_kmeans import ProgKMeans

df = pd.read_csv('../../sample_data/ross-df-256kp-500gvt_RbSec.csv')
X = np.array(df)

kmeans = ProgKMeans(n_clusters=3)
kmeans.progressive_fit(X, latency_limit_in_msec=10)
labels = kmeans.predict(X)

colors = [
    "#4b739d" if l == 0 else "#c74e52" if l == 1 else "#54944c" for l in labels
]
df = pd.DataFrame(X.transpose())
df.plot(color=colors, linewidth=0.25, legend=False, alpha=0.25)

# add one new feature for each data point
new_feature = np.random.rand(X.shape[0], 1) * X.max()
X = np.append(X, new_feature, 1)
kmeans.progressive_fit(X, latency_limit_in_msec=10)

# convert current labels to consistent labels with previous labels
labels, current_to_prev = kmeans.consistent_labels(labels, kmeans.predict(X))

colors = [
    "#4b739d" if l == 0 else "#c74e52" if l == 1 else "#54944c" for l in labels
]
df = pd.DataFrame(X.transpose())
df.plot(color=colors, linewidth=0.25, legend=False, alpha=0.25)

# simplified plot example
# visualize macro clusters
X_macro = np.array(kmeans.get_centers())
labels_macro = [current_to_prev[i] for i in range(X_macro.shape[0])]
colors_macro = [
    "#4b739d" if l == 0 else "#c74e52" if l == 1 else "#54944c"
    for l in labels_macro
]
df = pd.DataFrame(X_macro.transpose())
df.plot(color=colors_macro, linewidth=1, legend=False, alpha=0.5)

plt.show()
