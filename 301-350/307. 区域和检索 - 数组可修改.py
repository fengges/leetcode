import math
class NumArray:
    def __init__(self, nums):
        self.nums=nums
        self.n=int(math.sqrt(len(nums)))
        self.n=self.n if self.n*self.n==len(nums) else self.n+1
        self.size=len(nums)//self.n
        self.arr=[sum(self.nums[i:(i+1)*self.size]) for i in range(self.n)]

    def update(self, i, val):
        self.nums[i]=val

    def sumRange(self, i, j):
        return sum(self.nums[i:j+1])