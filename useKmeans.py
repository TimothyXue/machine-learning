from common.io.tsv import TsvDataSetReadr
from common.math import eulerDistance
from algorithm.kmeans import kMeans, randCent
import numpy as np
import matplotlib.pyplot as plt

dataReader = TsvDataSetReadr()
allData = dataReader.loadDataSet('kmeansPoints.txt', attrType=float)
dataMatrix = np.mat(allData)

centroids, clusterResult= kMeans(dataSet=dataMatrix, k=5, distOp=eulerDistance, centOp=randCent)
plt.subplot(111)
print(dataMatrix[:, 0].A)
plt.scatter(dataMatrix[:, 0].A.reshape(len(allData)), dataMatrix[:, 1].A.reshape(len(allData)))
plt.scatter(centroids[:, 0].A.reshape(centroids.shape[0]), centroids[:, 1].A.reshape(centroids.shape[0]))
plt.show()
#print(centroids)
#print(clusterResult)