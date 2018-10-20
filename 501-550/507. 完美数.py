import math
class Solution:
    def checkPerfectNumber(self, num):
        if num<=1:
            return False
        return sum([i+num/i for i in range(2,int(math.sqrt(num))+1) if num%i==0])==num-1
s=Solution()
test=[
{"input":  28, "output":True},
]

for t in test:
    r=s.checkPerfectNumber(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))