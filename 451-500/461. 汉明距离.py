class Solution:
    def hammingDistance(self, x, y):
        x1,y1=self.get(x),self.get(y)
        num=0
        for i in range(32):
            if x1[i]-y1[i]!=0:
                num+=1
        return num

    def get(self,n):
        tmp=[0 for i in range(32)]
        for i in range(32):
            if n&1==1:
                tmp[i]=1
            n=n>>1
        return tmp