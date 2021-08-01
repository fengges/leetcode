class Solution:
    def PredictTheWinner(self, nums):

        def func(l,r):
            if l==r:
                return nums[l]
            else:
                left=nums[l]-func(l+1,r)
                right=nums[r]-func(l,r-1)
                return max(left,right)
        return func(0,len(nums)-1)>0

