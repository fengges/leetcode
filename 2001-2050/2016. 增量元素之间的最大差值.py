class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        size=len(nums)
        ans=0
        for i in range(size):
            for j in range(i+1,size):

                ans=max(ans,nums[j]-nums[i])
        return ans if ans>0 else -1