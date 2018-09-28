def isBadVersion(version):
    return version>=5
class Solution:
    def firstBadVersion(self, n):
        l,r=1,n
        while l<r:
            m=int((l+r)/2)
            if isBadVersion(m):
                r=m
            else:
                l=m+1
        return l

s=Solution()
test=[
{"input":1000, "output":5},

]

for t in test:
    r=s.firstBadVersion(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.firstBadVersion(t['input'])