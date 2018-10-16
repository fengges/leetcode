class Solution:
    def binaryGap(self, N):
        num=self.count(N)
        num=[index for index,i in enumerate(num) if i==1]
        r=0
        for i in range(len(num)-1):
            r=max(r,num[i+1]-num[i])
        return r
    def count(self,n):
        sum=[]
        while n!=0:
            if n&1==1:
                sum.append(1)
            else:
                sum.append(0)
            n=n>>1
        return sum