class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        s=sum(nums)
        ans=0
        for i,v in enumerate(nums):
            ans+=v
            if ans>s/2:
                return nums[:i+1]
        return []