class Solution:
    def pivotArray(self, nums, pivot: int):
        return [n for n in nums if n<pivot]+[n for n in nums if n==pivot]+[n for n in nums if n>pivot]