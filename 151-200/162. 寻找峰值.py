class Solution:
    def findPeakElement(self, nums):
        for i in range(1,len(nums)-1):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                return i
        if nums[0]>nums[-1]:
            return 0
        return len(nums)-1