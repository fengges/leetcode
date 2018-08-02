class Solution:
    def moveZeroes(self, nums):
        start=0
        for index,value in enumerate(nums):
            if value==0:
                continue
            else:
                nums[start]=value
                start+=1
        for i in range(start,len(nums)):
            nums[i]=0