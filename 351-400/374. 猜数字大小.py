def guess(num):
    n=6
    if num<n:
        return 1
    elif num==n:
        return 0
    else:
        return -1
class Solution(object):
    def guessNumber(self, n):
        l,r=1,n
        while l<r:
            m=int((l+r)/2)
            t=guess(m)
            if t==0:
                return m
            elif t<0:
                r=m-1
            else:
                l=m+1
        return l

s=Solution()
test=[
{"input":10, "output":6},

]

for t in test:
    r=s.guessNumber(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.guessNumber(t['input'])