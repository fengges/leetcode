class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def dps(nums,index,sum):
            if index>=len(nums):
                return sum

            return dps(nums,index+1,sum^nums[index])+dps(nums,index+1,sum)
        return dps(nums,0,0)