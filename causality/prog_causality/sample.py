import numpy as np
import pandas as pd

from prog_causality import ProgCausality
from prog_inc_pca import ProgIncPCA

#
# 1. signle data point example
#
X = pd.read_csv('../../sample_data/ross-df-256kp-500gvt_kpgid100.csv')
# only take useful columns
metrics = [
    'NetworkRecv', 'NetworkSend', 'NeventProcessed', 'NeventRb', 'RbSec',
    'RbTotal', 'VirtualTimeDiff'
]
X = X[metrics]

# causality analysis
causality = ProgCausality()
# VAR with the progressive way
causality.adaptive_progresive_var_fit(X, latency_limit_in_msec=1000)
# causality.var_fit(X)
# Granger causality test from others to RbSec and RbSec to others
causality_from, causality_to = causality.check_causality('RbSec', signif=0.1)
# impulse response and variance decomposition
ir_from, ir_to = causality.impulse_response('RbSec')
vd_from, vd_to = causality.variance_decomp('RbSec')

# print results
print('KpGid = 100')
print('Rbsec (caused by)')
print(
    pd.DataFrame({
        'Metrics': metrics,
        'Causality': causality_from,
        'IR 1 step later': ir_from[:, 1],
        'VD 1 step later': vd_from[:, 1]
    }))

print('Rbsec (causing to)')
print(
    pd.DataFrame({
        'Metrics': metrics,
        'Causality': causality_to,
        'IR 1 step later': ir_to[:, 1],
        'VD 1 step later': vd_to[:, 1]
    }))

#
# 2. multiple data points with PCA
#
# apply progressive PCA for each metric to reduce dimensions (multiple time-series) to 1D (single time-series)
pca = ProgIncPCA(n_components=1)
total_latency_for_pca = 100
latency_for_each = int(total_latency_for_pca / len(metrics))
X_dict = {}
for metric in metrics:
    # load data. col header: Last GVT, shape of rest: (n, d). n: # of kps, d: # of time points
    file_name = '../../sample_data/ross-df-256kp-500gvt_' + metric + '.csv'
    metric_nd = pd.read_csv(file_name)
    pca.progressive_fit(
        metric_nd,
        latency_limit_in_msec=latency_for_each,
        point_choice_method='reverse')
    metric_1d = pca.transform(metric_nd)
    X_dict[metric] = metric_1d.flatten().tolist()
X = pd.DataFrame(X_dict)

# causality analysis
causality = ProgCausality()
causality.adaptive_progresive_var_fit(X, latency_limit_in_msec=100)
causality_from, causality_to = causality.check_causality('RbSec', signif=0.1)
ir_from, ir_to = causality.impulse_response('RbSec')
vd_from, vd_to = causality.variance_decomp('RbSec')

# print results
print('All KPs')
print('Rbsec (caused by)')
print(
    pd.DataFrame({
        'Metrics': metrics,
        'Causality': causality_from,
        'IR 1 step later': ir_from[:, 1],
        'VD 1 step later': vd_from[:, 1]
    }))

print('Rbsec (causing to)')
print(
    pd.DataFrame({
        'Metrics': metrics,
        'Causality': causality_to,
        'IR 1 step later': ir_to[:, 1],
        'VD 1 step later': vd_to[:, 1]
    }))
