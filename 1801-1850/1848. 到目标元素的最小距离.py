class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        ans=[i for i,v in enumerate(nums) if v==target]
        return min([abs(a-start) for a in ans ])