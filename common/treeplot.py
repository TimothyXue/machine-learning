import matplotlib.pyplot as plt

ARROW_ARGS = dict(arrowstyle="<-")
START_AXIS = 0.1
END_AXIS = 0.9
AXIS_DISTANCE = END_AXIS - START_AXIS
DECISION_NODE = dict(boxstyle='sawtooth', fc='#cab3f0')
LEAF_NODE = dict(boxstyle='round4', fc='#c8dcc8')


class TreePlot:
    def __init__(self):
        self.ax1 = plt.subplot(1, 1, 1, frameon=False)
        pass

    def plotTree(self, tree):
        if tree.root is None:
            return

        startY = END_AXIS
        treeHeight = tree.getHeight()
        distanceY = AXIS_DISTANCE
        if treeHeight > 1:
            distanceY = AXIS_DISTANCE / (tree.getHeight() - 1)
        startX = START_AXIS
        endX = END_AXIS

        self.plotTreeNode(tree.root, startX, endX, startY, distanceY)
        plt.show()

    def plotTreeNode(self, treeNode, startX, endX, startY, distanceY, **kwargs):
        nodeStyle = LEAF_NODE if treeNode.isLeaf() else DECISION_NODE

        centerPt = ((endX - startX) / 2 + startX, startY)
        parentPt = kwargs.get('parentPt', centerPt)
        edgeLabel = kwargs.get('edgeLabel', None)

        self.plotNode(treeNode.label, centerPt, parentPt, nodeStyle)
        if edgeLabel is not None:
            self.plotText(edgeLabel, centerPt, parentPt)

        childrenCount = len(treeNode.children)
        if childrenCount == 1:
            distanceX = 0
            startX = endX = centerPt[0]
        else:
            distanceX = endX - startX
        startY -= distanceY

        totalWidth = treeNode.getWidth()
        for childEdgeLabel, childNode in treeNode.children.items():
            childWidth = childNode.getWidth()
            endX = startX + distanceX * childWidth / totalWidth

            self.plotTreeNode(childNode, startX, endX, startY, distanceY,
                              parentPt=centerPt, edgeLabel=childEdgeLabel)
            startX = endX

    def plotNode(self, nodeTxt, centerPt, parentPt, nodeType):
        self.ax1.annotate(nodeTxt, xy=parentPt, xycoords='axes fraction',
                          xytext=centerPt, textcoords='axes fraction',
                          va='center', ha='center', bbox=nodeType, arrowprops=ARROW_ARGS)

    def plotText(self, text, centerPt, parentPt):
        xMid = (parentPt[0] + centerPt[0]) / 2.0
        yMid = (parentPt[1] + centerPt[1]) / 2.0
        self.ax1.text(xMid, yMid, text)
