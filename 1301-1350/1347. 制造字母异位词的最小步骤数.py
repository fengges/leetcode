from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        a=Counter(s)
        b=Counter(t)
        key=a.keys()|b.keys()
        ans=0
        for k in key:
            ans+=abs(a.get(k,0)-b.get(k,0))
        return ans//2
s=Solution()
null=None
test=[
    {"input":['aba','bab'],"output":1},

]
for t in test:
    r=s.minSteps(*t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))