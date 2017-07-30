from common.io.tsv import TsvDataSetReadr
from algorithm.apriori import apriori, calculateAssociativeRule

dataReader = TsvDataSetReadr()
transactions = dataReader.loadDataSet('aprioriData.txt')

itemSetsList, supports = apriori(transactions, supportThreshold=0.5)
calculateAssociativeRule(itemSetsList, supports)
print(transactions)
print(itemSetsList)
print(supports)
