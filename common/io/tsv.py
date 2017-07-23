class TsvDataSetReadr(object):
    def __init__(self):
        pass

    def loadDataSet(self, fileName, **kwargs):
        attrType = kwargs.get('attrType', None)
        dataFile = open(fileName, 'r', encoding='utf-8')
        lines =dataFile.readlines()

        matrix = [self.parseLine(line, attrType=attrType) for line in lines]
        return matrix

    def parseLine(self, line, **kwargs):
        attrType = kwargs.get('attrType', None)

        #create x and y vai '\t'
        words = line.strip().split('\t')
        if attrType is None:
            return words

        #convert string array to floating type based array
        return [attrType(word) for word in words]
