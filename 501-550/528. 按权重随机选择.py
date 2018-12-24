import random
class Solution:
    def __init__(self, w):
        sum=0
        self.list=[-1]
        for i in range(len(w)):
            sum+=w[i]
            self.list.append(sum)
    def getNum(self,n):
        print(n)
        size=len(self.list)-1
        left,right=0,size
        while left<=right:
            mid=int((left+right)/2)
            if self.list[mid]<=n and self.list[mid+1]>n:
                return mid
            elif self.list[mid]>n:
                right=mid
            else:
                left=mid
        return mid
    def pickIndex(self):
        n=random.randint(0,self.list[-1]-1)
        return self.getNum(n)

t=Solution([3,14,1,7])
print(t.pickIndex())
