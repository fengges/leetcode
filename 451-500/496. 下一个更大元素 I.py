class Solution:
    def nextGreaterElement(self, nums1, nums2):
        r=[]
        for n in nums1:
            r.append(self.find(n,nums2))
        return r
    def find(self,n,nums):
        index=nums.index(n)
        for i in range(index,len(nums)):
            if nums[i]>n:
                return nums[i]
        return -1