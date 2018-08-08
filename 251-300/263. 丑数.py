class Solution:
    def isUgly(self, num):
        if num==0:
            return False
        while num!=1:
            if num%2==0:
                num=num/2
                continue
            elif num%3==0:
                num=num/3
                continue
            elif num%5==0:
                num=num/5
                continue
            return False
        return True

s=Solution()
test=[
{"input": 0, "output":False},
{"input": 6, "output":True},
{"input": 14, "output":False},
]

for t in test:
    r=s.isUgly(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.isUgly(t['input'])