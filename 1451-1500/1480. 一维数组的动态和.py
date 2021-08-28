class Solution:
    def runningSum(self, nums):
        ans=0
        t=[]
        for n in  nums:
            ans+=n
            t.append(ans)
        return t