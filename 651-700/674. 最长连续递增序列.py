class Solution:
    def findLengthOfLCIS(self, nums):
        if len(nums)==0:
            return 0
        maxL=1
        l=1
        for i in range(len(nums)-1):
            if nums[i+1]>nums[i]:
                l+=1
                maxL=max(l,maxL)
            else:
                l=1
        return maxL

s = Solution()
test = [
{"input": [1,3,5,4,7], "output": 3},
{"input": [2,2,2,2,2], "output": 1},

]

for t in test:
    r = s.findLengthOfLCIS(t['input'])
    if r != t['output']:
        print("error:" + str(t) + " out:" + str(r))
        r = s.findLengthOfLCIS(t['input'])