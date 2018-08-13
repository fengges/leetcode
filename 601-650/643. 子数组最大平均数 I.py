class Solution:
    def findMaxAverage(self, nums, k):
        if len(nums)==1:
            return nums[0]
        sum=0
        for i in range(k):
            sum+=nums[i]
        max=sum
        for i in range(len(nums)-k):
            sum=sum-nums[i]+nums[i+k]
            if sum>max:
                max=sum
        return max/k
