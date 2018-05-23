class Solution:
    def getIndex(self,nums,target):
        left=0
        right=len(nums)-1
        while left<=right:
            min=int((left+right)/2)
            if nums[min]==target:
                return min
            elif nums[min]>target:
                right = min - 1
            else:
                left = min + 1
        return -1
    def search(self, nums, target):
        pass
