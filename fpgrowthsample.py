from common.io.tsv import TsvDataSetReadr
from common.treeplot import TreePlot
from algorithm.fpgrowth import FpTree

dataReader = TsvDataSetReadr()
transactions = dataReader.loadDataSet('fpGrowthData.txt')

fpTree = FpTree(transactions, supportThreshold=0.5)
treePlot = TreePlot()
treePlot.plotTree(fpTree)