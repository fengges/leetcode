import collections
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dicts=collections.Counter(nums)
        ans=0
        for d in dicts:
            if dicts[d]==1:
                ans+=d
        return ans