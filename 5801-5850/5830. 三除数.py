import math
class Solution:
    def isThree(self, n: int) -> bool:
        if n==1:
            return False
        t=math.sqrt(n)
        if t==int(t):
            a=int(math.sqrt(t))+1
            for i in range(2,a):
                if t%i==0:
                    return False
            return True
        else:
            return False

s=Solution()
null=None
test=[
    {"input":121,"output":True},
    {"input":2,"output":False},
    {"input":4,"output":True},
    {"input":12,"output":False},
    {"input":81,"output":False},

]
for t in test:
    r=s.isThree(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))