import math
class Solution:
    def missingTwo(self, nums) :
        N=len(nums)+2
        x=N*(N+1)//2-sum(nums)
        ans=1
        for a in range(1,N+1):
            ans*=a
        for a in nums:
            ans//=a
        y=ans
        a=int(x+math.sqrt(x*x-4*y))//2
        return [a,x-a]

s=Solution()
null=None
test=[
    {"input":[1],"output":True},

]
for t in test:
    r=s.missingTwo(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))