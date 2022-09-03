import collections
class Solution:
    def findCenter(self, edges) -> int:
        ans=[]
        for e in edges:
            ans.extend(e)
        ans=collections.Counter(ans)
        return max(ans.items(),key=lambda x:x[1])[0]
s=Solution()

test=[
    {"input":[[1,2],[2,3],[4,2]],"output":2},

]
for t in test:
    r=s.findCenter(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))