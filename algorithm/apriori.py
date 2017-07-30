from itertools import combinations
"""Apriori implementation"""


def apriori(transactions, supportThreshold):
    """Aprioir implementation"""
    # Transfer the transaction to set
    transactionSets = [set(transaction) for transaction in transactions]
    # Generate the 1 item Set
    itemSets = createItemSets(transactions)
    # filter the 1 item Set by threshold, and count each matched item's support
    filteredItemSets, supports = filterBySupport(transactionSets, itemSets, supportThreshold)
    itemSetsList = [filteredItemSets]

    # When the filtered Item Set is empty, then stop the finding
    while len(filteredItemSets) > 0:
        itemSets = combineItemSets(itemSets)
        # filter again
        filteredItemSets, newSupports = filterBySupport(transactionSets, itemSets, supportThreshold)
        supports.update(newSupports)

        itemSetsList.append(filteredItemSets)

    return itemSetsList, supports


def createItemSets(transactions):
    # initialize an item Set
    itemSets = []
    # Traverse all the transaction
    for transaction in transactions:
        for item in transaction:
            itemSet = [item]

            if itemSet not in itemSets:
                itemSets.append(itemSet)
    # sort and frozenset
    itemSets.sort()
    return [frozenset(itemSet) for itemSet in itemSets]


def filterBySupport(transactions, itemSets, supportThreshold):
    itemSetCounts = {}

    # Traverse the transcation and count the item showing times
    for transcation in transactions:
        for itemSet in itemSets:
            if itemSet.issubset(transcation):
                #default zero
                itemSetCount = itemSetCounts.get(itemSet, 0)
                itemSetCounts[itemSet] = itemSetCount + 1

    filteredItems = []
    supports = {}
    transactionCount = len(transactions)

    for itemSet, itemSetCount in itemSetCounts.items():
        # Calculate the support of each item
        support = itemSetCount / transactionCount
        if support > supportThreshold:
            filteredItems.append(itemSet)

        supports[itemSet] = support

    return filteredItems, supports


def combineItemSets(itemSets):
    newItemSets = []
    itemSetsCount = len(itemSets)

    # Traverse the item set to compare and combine
    for itemSet1Index in range(itemSetsCount):
        for itemSet2Index in range(itemSet1Index + 1, itemSetsCount):
            itemSet1 = itemSets[itemSet1Index]
            itemSet2 = itemSets[itemSet2Index]

            #Count the different Set
            diff1 = itemSet1 - itemSet2
            diff2 = itemSet2 - itemSet1

            if len(diff1) == 1 and len(diff2) == 1:
                newItemSet = itemSet1 | itemSet2
                if newItemSet not in newItemSets:
                    newItemSets.append(newItemSet)

    return newItemSets


def calculateAssociativeRule(itemSetsList, supports):
    confidenceList = {}
    for itemSets in itemSetsList:
        for itemSet in itemSets:
            if len(itemSet) < 2:
                break
            else:
                for indexCount in range(1, len(itemSet)):
                    generator = combinations(itemSet, indexCount)
                    for item in generator:
                        confidenceItem = frozenset(item)
                        diffItemSet = itemSet - confidenceItem
                        itemSupport = supports.get(confidenceItem, 0)
                        itemSetSupport = supports.get(itemSet, 0)
                        confidence = itemSetSupport / itemSupport
                        print('%r -> %r : %f' % (confidenceItem, diffItemSet, confidence))
