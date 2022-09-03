class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            sum = nums[l] + nums[r]
            if sum == target:
                return [nums[l], nums[r]]
            elif sum > target:
                r -= 1
            else:
                l += 1
        return []