import sys
class Solution(object):
    def find132pattern(self, nums):
        n = len(nums)
        if n < 3:
            return False
        stack = []
        third_nums = -sys.maxsize
        for i in range(len(nums)):
            if nums[n - 1 - i] < third_nums:
                return True
            while (len(stack) >= 1) and (nums[n - 1 - i] > stack[-1]):
                third_nums = stack.pop(-1)
            stack.append(nums[n - 1 - i])

        return False

s = Solution()
test = [
    {"input":  [1, 2, 3, 4],"output":False},
    {"input": [3, 1, 4, 2], "output": True},
    {"input":  [-1, 3, 2, 0], "output": True},
]

for t in test:
    r = s.find132pattern(t['input'])
    if r != t['output']:
        print("error:" + str(t) + " out:" + str(r))