from heapq import *
class MedianFinder:
    def __init__(self):
        self.minlist=[]
        self.maxlist = []
    def addNum(self, num):
        if num > self.findMedian():
            heappush(self.maxlist, num)
        else:
            heappush(self.minlist, num)
        len1, len2 = len(self.maxlist), len(self.minlist)
        if len1<len2:
            self.maxlist.append(self.minlist.pop())
        elif len1>len2+1:
            self.minlist.append(self.maxlist.pop())

    def findMedian(self):
        len1,len2=len(self.maxlist),len(self.minlist)
        if len1+len2==0:
            return 0
        elif len1==len2:
            return (self.minlist[-1]+self.maxlist[-1])/2
        else:
            return self.maxlist[-1]

t=MedianFinder()
t.addNum(1)
t.addNum(2)
print(t.findMedian())
t.addNum(3)
print(t.findMedian())
