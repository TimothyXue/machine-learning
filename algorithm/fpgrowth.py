from common.tree import Tree, TreeNode


class FpTreeNode(TreeNode):
    def __init__(self, name, count, parent):
        label = '{name}: {count}'.format(name=name, count=count)
        super(FpTreeNode, self).__init__(label=label)

        self.name = name
        self.count = count
        self.parent = parent
        self.nextNode = None

    def addCount(self, count):
        self.count += count
        self.label = '{name}: {count}'.format(name=self.name, count=self.count)


class FpTree(Tree):
    def __init__(self, transactions, supportThreshold):
        super(FpTree, self).__init__(root=FpTreeNode(name="root", count=0, parent=None))

        self.supportThreshold = supportThreshold
        self.items = []
        self.itemsCounts = {}
        self.headerTable = {}

        self.createTree(transactions)

    def createTree(self, transactions):
        self.items, self.itemsCounts, transactions = self.filterItemsBySupport(transactions)
        self.sortTransactions(transactions)

        for transaction in transactions:
            self.updateTree(transaction, self.root)

    def filterItemsBySupport(self, transactions):
        transactions = [set(transaction) for transaction in transactions]
        itemCounts = {}

        for transaction in transactions:
            for item in transaction:
                itemCount = itemCounts.get(item, 0)
                itemCounts[item] = itemCount + 1

        filteredItems = []
        transactionCount = len(transactions)

        for item, itemCount in itemCounts.items():
            support = itemCount / transactionCount

            if support >= self.supportThreshold:
                filteredItems.append({
                    'name': item,
                    'count': itemCount
                })
            else:
                for transaction in transactions:
                    if item in transaction:
                        transaction.remove(item)
        filteredTransactions = [list(transaction) for transaction in transactions]
        return filteredItems, itemCounts, filteredTransactions

    def sortTransactions(self, transactions):
        for transaction in transactions:
            transaction.sort(key=lambda itemName: self.itemsCounts[itemName], reverse=True)

    def updateTree(self, items, treeNode):
        if len(items) == 0:
            return

        item = items[0]

        if item not in treeNode.children:
            childNode = FpTreeNode(name=item, count=0, parent=treeNode)
            treeNode.children[item] = childNode
            self.updateHeaderTable(item, childNode)

        childNode = treeNode.children[item]
        childNode.addCount(1)

        self.updateTree(items[1:], childNode)

    def updateHeaderTable(self, item, childNode):

        if item not in self.headerTable:
            self.headerTable[item] = childNode
        else:
            currentNode = self.headerTable[item]
            while currentNode.nextNode is not None:
                currentNode = currentNode.nextNode

            currentNode.nextNode = childNode


