import math
class Solution:
    def consecutiveNumbersSum(self, N):
        result=[]
        if N==1:
            return 1
        for i in range(1, N):
            a=(2*N-i*i+i)/2/i
            if a<=0:
                break
            if a!=int(a) :
                continue
            temp=[]
            for j in range(i):
                temp.append(a+j)
            result.append(temp)
        return len(result)

s=Solution()
test=[

{"input": 855204, "output":4},
{"input": 15, "output":4},
{"input": 9, "output":3},
{"input": 5, "output":2},
]

for t in test:
    r=s.consecutiveNumbersSum(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.consecutiveNumbersSum(t['input'])

