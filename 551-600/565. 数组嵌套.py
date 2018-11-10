class Solution(object):
    def arrayNesting(self, nums):
        dic={}
        flag=[True for i in nums]
        for i in range(len(nums)):
            if flag[i]:
                dic[nums[i]]=[nums[i]]
                while True:
                    pass