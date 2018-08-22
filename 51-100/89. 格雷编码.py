import math
class Solution:
    def grayCode(self, n):
        r=[0,1]
        if n==0:
            return [0]
        elif n==1:
            return r
        for i in range(1,n):
            t=[]
            for j in range(len(r)-1,-1,-1):
                t.append(r[j]+int(math.pow(2,i)))
            r.extend(t)

        return r

s=Solution()
test=[
{"input": 2, "output":[0,1,3,2]},
{"input": 3, "output":[0,1,3,2]},
]

for t in test:
    r=s.grayCode(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.grayCode(t['input'])