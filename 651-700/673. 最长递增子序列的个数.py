class Solution:
    def findNumberOfLIS(self, nums):
        if len(nums)==0:
            return 0
        maxL=1
        l=1
        m=len(nums)
        for i in range(len(nums)-1):
            if nums[i+1]>nums[i]:
                l+=1
                if l==maxL:
                    m+=1
                elif l>maxL:
                    maxL=l
                    m=1
            else:
                l=1
        return m