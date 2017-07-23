import numpy as np


def randCent(dataSet, k):
    # generate cent randomly
    n = np.shape(dataSet)[1]
    centroids = np.mat(np.zeros((k, n)))

    for j in range(n):
        # retrieve minimum from shape n
        minJ = min(dataSet[:, j])
        rangeJ = float(max(dataSet[:, j] -minJ))

        centroids[:, j] = minJ + rangeJ * np.random.rand(k, 1)

    return centroids


def kMeans(dataSet, k, distOp, centOp):
    centroids = centOp(dataSet, k)

    dataCount = np.shape(dataSet)[0]
    clusterResult = np.mat(np.zeros((dataCount, 2)))

    #todo...
    while True:
        clusterChanged = clusterData(centroids, clusterResult, dataCount, dataSet, distOp, k)
        if not clusterChanged:
            break

            #reset
            resetCentroids(centroids, clusterResult, dataSet, k)

    return centroids, clusterResult


def resetCentroids(centroids, clusterResult, dataSet, k):
    for centIndex in range(k):
        clusterMap = clusterResult[:, 0].A == centIndex
        clusterPointIndexes = np.nonzero(clusterMap)[0]

        clusterPoints = dataSet[clusterPointIndexes]

        centroids[centIndex, :] = np.mean(clusterPoints, axis=0)


def clusterData(centroids, clusterResult, dataCount, dataSet, distOp, k):
    #cluster data using cents
    clusterChanged = False
    for datumIndex in range(dataCount):
        datum = dataSet[datumIndex, :]
        minDist, minIndex = findMinCent(datum, centroids, k, distOp)
        if clusterResult[datumIndex, 0] != minIndex:
            clusterChanged = True
        #record cluster result
        clusterResult[datumIndex, :] = minIndex, minDist ** 2

    return clusterChanged


def findMinCent(datum, centroids, k, distOp):
    minDist = np.inf
    minIndex = -1

    #traverse centroids
    for centroidsIndex in range(k):
        centroid = centroids[centroidsIndex, :]
        dist = distOp(datum, centroid)

        if dist < minDist:
            minDist = dist
            minIndex = centroidsIndex

    return minDist, minIndex