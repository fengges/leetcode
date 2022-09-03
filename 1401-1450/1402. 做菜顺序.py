class Solution:
    def maxSatisfaction(self, satisfaction) -> int:
        satisfaction.sort(reverse=True)
        ans=0
        suma=0
        for  s in  satisfaction:
            suma+=s
            ans=max(ans+suma,ans)
        return ans

s=Solution()
null=None
test=[
    {"input": [-1,-8,0,5,-7],"output":14},


]
for t in test:
    r=s.maxSatisfaction(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))