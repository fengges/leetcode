class Solution:
    def findErrorNums(self, nums):
        return [self.findDuplicate(nums),self.missingNumber(nums)]
    def findDuplicate(self, nums):
        dic={}
        for n in nums:
            if n in dic:
                dic[n]+=1
            else:
                dic[n]=1
        for k in dic:
            if dic[k]==2:
                return k
    def missingNumber(self, nums):
        nums.sort()
        if nums[0] != 1:
            return 1
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] > 1:
                return nums[i] + 1
        return nums[-1] + 1