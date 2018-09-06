class Solution:
    def search(self, nums, target):
        l,r=0,len(nums)-1
        while l<=r:
            m=int((l+r)/2)
            if nums[m]==target:
                return m
            if nums[m]<target:
                l=m+1
            else:
                r=m-1
        return -1