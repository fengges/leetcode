class PeekingIterator:
    def __init__(self, iterator):
        self.s=0
        self.data=[]
        while iterator.hasNext():
            val =iterator.next()
            self.data.append(val)

    def peek(self):
        if self.hasNext():
            return self.data[self.s]


    def next(self):
        if self.hasNext():
            self.s+=1
            return self.data[self.s-1]

    def hasNext(self):
        return self.s<len(self.data)