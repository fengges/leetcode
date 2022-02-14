class Solution:
    def minimumDifference(self, nums, k: int) -> int:
        nums.sort()
        ans=nums[-1]-nums[0]
        for i in range(len(nums)-k+1):
            ans=min(ans,nums[i+k-1]-nums[i])
        return ans

s=Solution()

test=[
    {"input": [[9,4,1,7],2],"output":2},

]
for t in test:
    r=s.minimumDifference(*t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
