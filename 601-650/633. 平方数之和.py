class Solution:
    def judgeSquareSum(self, c):
        l,r=0,int(self.sqrt(c))+1
        while l<=r:
            t=l*l+r*r
            if t==c:
                return True
            elif t<c:
                l+=1
            elif t>c:
                r-=1
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
{"input":2, "output":True},
]

for t in test:
    r=s.judgeSquareSum(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
