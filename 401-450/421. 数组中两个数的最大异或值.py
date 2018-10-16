class Solution:
    def findMaximumXOR(self, nums):
        m=0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                m=max(m,nums[i]^nums[j])
        return m