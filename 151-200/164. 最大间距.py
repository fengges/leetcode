class Solution:
    def maximumGap(self, nums):
        nums.sort()
        m=0
        for i in range(len(nums)-1):
            m=max(m,nums[i+1]-nums[i])
        return m
