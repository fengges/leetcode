class NestedIterator(object):
    def __init__(self, nestedList):
        self.list=[]
        self.add(self.list,nestedList)
        self.index=0
    def add(self,list,nestedList):
        for tmp in nestedList:
            if tmp.isInteger():
                list.append(tmp.getInteger())
            else:
                self.add(list,tmp.getList())
    def next(self):
        self.index+=1
        return self.list[self.index-1]

    def hasNext(self):
        return len(self.list)!=self.index
