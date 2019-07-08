import random
class Solution:
    def __init__(self, nums):
        self.nums=nums
        self.index = [i for i in range(len(self.nums))]
    def reset(self):
        self.index = [i for i in range(len(self.nums))]
    def shuffle(self):
        random.shuffle(self.index)
        return self.getArray()
    def getArray(self):
        num=[self.nums[i] for i in self.index]
        return num