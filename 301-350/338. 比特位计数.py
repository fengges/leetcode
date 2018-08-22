class Solution(object):
    def countBits(self, num):
        r=[]
        for i in range(num+1):
            r.append(self.count(i))
        return r
    def count(self,n):
        num=0
        for i in range(32):
            if n&1==1:
                num+=1
            n=n>>1
        return num