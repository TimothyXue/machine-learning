class TreeNode(object):
    def __init__(self, label, **kwargs):
        self.label = label
        self.children = kwargs.get('children', {})

    def isLeaf(self):
        return len(self.children) == 0

    def getHeight(self):
        if self.isLeaf():
            return 1

        return 1 + max([child.getHeight() for child in self.children.values()])

    def getWidth(self):
        if self.isLeaf():
            return 1

        return sum([child.getWidth() for child in self.children.values()])


class Tree(object):
    def __init__(self, **kwargs):
        self.root = kwargs.get('root', None)

    def getHeight(self):
        if self.root is None:
            return 0

        return self.root.getHeight()

    def getWidth(self):
        if self.root is None:
            return 0

        return self.root.getWidth()
