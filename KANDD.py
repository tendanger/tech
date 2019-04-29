from sklearn.datasets.samples_generator import make_moons
import matplotlib.pyplot as plt

import time
from sklearn.cluster import KMeans

from sklearn.cluster import DBSCAN

X, y_true = make_moons(n_samples=1000, noise=0.15)

plt.scatter(X[:, 0], X[:, 1], c=y_true)
plt.show()

# Kmeans
t0 = time.time()
kmeans = KMeans(init='k-means++', n_clusters=2, random_state=8).fit(X)
t = time.time() - t0
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_)
plt.title('time : %f' % t)
plt.show()

# DBSCAN
t0 = time.time()
dbscan = DBSCAN(eps=.1, min_samples=6).fit(X)
print(dbscan.components_.shape)
print(dbscan.core_sample_indices_)
t = time.time() - t0
plt.scatter(X[:, 0], X[:, 1], c=dbscan.labels_)
plt.title('time : %f' % t)
plt.show()
