class Solution:
    def rob(self, nums):
        flag=[0 for i in range(len(nums)+2)]
        for i in range(len(nums)):
            flag[i+2]=max(flag[i]+nums[i],flag[i+1])
        return flag[-1]