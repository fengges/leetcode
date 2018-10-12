class Solution:
    def isPerfectSquare(self, num):
        i=0
        while True:
            t=i*i
            if t==num:
                return True
            elif t>num:
                return False
            i+=1
        return False
    def sqrt(self,x):
        if x == 0:
            return 0
        old = x
        while True:
            new = (old + x / old) / 2
            if abs(new - old) < 0.000000001:
                break
            old = new

        return new

s=Solution()
test=[
{"input": 16, "output":True},
]

for t in test:
    r=s.isPerfectSquare(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))