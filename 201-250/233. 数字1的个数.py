class Solution:
    def countDigitOne(self, n):
        r=0
        for i in range(n+1):
            t=str(i)
            for  j in t:
                if j=='1':
                    r+=1
        return r