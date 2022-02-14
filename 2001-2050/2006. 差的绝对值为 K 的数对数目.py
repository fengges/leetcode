class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        size=len(nums)
        ans=0
        for i in range(size):
            for j in range(1+i,size):
                if abs(nums[i]-nums[j])==k:
                    ans+=1
        return ans