class Solution:
    def arrayPairSum(self, nums):
         nums.sort()
         i=0
         sum=0
         while i<len(nums):
             sum+=nums[i]
             i+=2
         return sum
s = Solution()
test = [
    {"input": [1,4,3,2], "output":4},
]

for t in test:
    r = s.arrayPairSum(t['input'])
    if r != t['output']:
        print("error:" + str(t) + " out:" + str(r))
        r = s.arrayPairSum(t['input'])