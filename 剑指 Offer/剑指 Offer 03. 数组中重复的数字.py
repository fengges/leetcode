import collections
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        dicts=collections.Counter(nums)
        return [k for k in dicts if dicts[k]>1]
