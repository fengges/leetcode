class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        ans=0
        start=0
        for e in range(len(nums)):
            while( nums[e]-nums[start]>1):
                start+=1
            if nums[e]-nums[start]==1:
                ans=max(ans,e-start+1)
        return ans