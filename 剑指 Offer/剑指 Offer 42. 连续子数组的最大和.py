class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max=nums[0]
        sum=0
        for n in nums:
            sum+=n
            if sum>max:
                max=sum
            if sum<0:
                sum=0
        return max