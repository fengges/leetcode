class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans=0
        size=len(nums)
        for i in range(size):
            for j in range(i+1,size):
                if nums[i]==nums[j]:
                    ans+=1
        return ans