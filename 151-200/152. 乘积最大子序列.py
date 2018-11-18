class Solution:
    def maxProduct(self, nums):
        size=len(nums)
        if size==1:
            return nums[0]
        r,mmax,mmin=nums[0],nums[0],nums[0]
        for i in range(1,size):
            if nums[i]>0:
                mmax=max(mmax*nums[i],nums[i])
                mmin=min(mmin*nums[i],nums[i])
            else:
                tmp=mmax
                mmax=max(mmin*nums[i],nums[i])
                mmin=min(tmp*nums[i],nums[i])
            r=max(r,mmax)
        return r