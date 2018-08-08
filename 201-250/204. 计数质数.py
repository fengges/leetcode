import math
class Solution:
    def countPrimes(self, n):
        if n<2:
            return 0

        num=0
        r=[0 for i in range(n+1)]
        for i in range(2,n+1):
            if r[i]==0:
                for j in range(i+i,n+1,i):
                    r[j]=1
        for i in range(2,n+1):
            if r[i]==0:
                num+=1
        return num




s=Solution()

test=[
{"input":10,"output":4},
{"input":499979,"output":4},

]


for t in test:
    r=s.countPrimes(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))