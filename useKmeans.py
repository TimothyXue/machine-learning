from common.io.tsv import TsvDataSetReadr
from common.math import eulerDistance
from algorithm.kmeans import kMeans, randCent
import numpy as np

dataReader = TsvDataSetReadr()
allData = dataReader.loadDataSet('kmeansPoints.txt', attrType=float)
dataMatrix = np.mat(allData)

centroids, clusterResult= kMeans(dataSet=dataMatrix, k=5, distOp=eulerDistance, centOp=randCent)
print(centroids)
print(clusterResult)