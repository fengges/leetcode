class Solution:
    def maxSubArray(self, nums):
        max=nums[0]
        sum=0
        for n in nums:
            sum+=n
            if sum>max:
                max=sum
            if sum<0:
                sum=0
        return max


s = Solution()

test = [
    {"input": [-1], "output": -1},
    {"input":[-2,1,-3,4,-1,2,1,-5,4], "output":6}
]

for t in test:
    r = s.maxSubArray(t['input'])
    if r != t['output']:
        print("error:" + str(t) + " out:" + str(r))
        r = s.maxSubArray(t['input'])
