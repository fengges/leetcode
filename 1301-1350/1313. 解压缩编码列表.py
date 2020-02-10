class Solution:
    def decompressRLElist(self, nums):
        def func(a,b):
            return [b for i in range(a)]
        ans=[]
        for i in range(len(nums)//2):
            t=func(nums[2*i],nums[2*i+1])
            ans.extend(t)
        return ans
