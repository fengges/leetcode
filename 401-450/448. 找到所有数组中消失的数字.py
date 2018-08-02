class Solution:
    def findDisappearedNumbers(self, nums):
        r=[]
        if len(nums)==0:
            return r
        nums.sort()
        for i in range(1,nums[0]):
            r.append(i)
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] > 1:
                for j in range(nums[i]+1,nums[i+1]):
                    r.append(j)
        for i in range(nums[-1]+1,len(nums)+1):
            r.append(i)
        return r