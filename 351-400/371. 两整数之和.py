class Solution:
    def getSum(self, a, b):
        reuslt=(a^b)% 0x100000000
        forword=(a&b)<<1% 0x100000000
        if forword==0:
            return reuslt if reuslt <= 0x7FFFFFFF else reuslt | (~0x100000000+1)
        else:
            return self.getSum(reuslt,forword)
s=Solution()

test=[
{"input":[-8,-12],"output": 2},
{"input":[1,-1],"output": 0},
]
for t in test:
    r=s.getSum(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))