class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        size=len(nums)
        return max([(nums[i]-1)*(nums[j]-1) for i in range(size) for j in range(i+1,size)])