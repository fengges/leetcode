import math
class Solution:

    def reverseBits(self, n):
        tmp=[0 for i in range(32)]
        for i in range(32):
            if n&1==1:
                tmp[i]=1
            n=n>>1
        sum=0
        for i in range(32):
            sum+=tmp[31-i]*math.pow(2,i)
        return int(sum)

s=Solution()
test=[
{"input":     43261596, "output":1},
]

for t in test:
    r=s.reverseBits(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.reverseBits(t['input'])