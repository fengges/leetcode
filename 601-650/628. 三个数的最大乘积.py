class Solution:
    def maximumProduct(self, nums):
        nums.sort()
        if 0 in nums:
            nums.remove(0)
        if len(nums)<3:
            return 0
        return max(nums[0]*nums[1]*nums[-1],nums[-1]*nums[-2]*nums[-3])