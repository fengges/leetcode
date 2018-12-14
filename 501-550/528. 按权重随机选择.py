import math,random
class Solution:
    def __init__(self, w):
        n=len(w)
        self.size=int((n+1)*n/2)-1
        self.list=w
    def getNum(self,n):
        return int((math.sqrt(8*n+1)-1)/2)

    def pickIndex(self):
        n=random.randint(0,self.size)
        return self.list[self.getNum(n)]
