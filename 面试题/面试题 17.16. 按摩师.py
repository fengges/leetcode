class Solution:
    def massage(self, nums: List[int]) -> int:
        size=len(nums)
        ans=[0 for i in range(size+2)]
        for i in range(size):
            ans[i+2]=max(ans[i+1],ans[i]+nums[i])
        return ans[-1]