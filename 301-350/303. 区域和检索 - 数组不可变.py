class NumArray:
    def __init__(self, nums):
        self.nums=nums

    def sumRange(self, i, j):
        return sum(self.nums[i:j+1])