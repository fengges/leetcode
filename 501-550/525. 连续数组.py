class Solution:
    def findMaxLength(self, nums):
        result=[0]
        sum=0
        maxL=0
        dic={0:-1}
        for i in range(len(nums)):
            if nums[i]==0:
                nums[i]=-1
            sum+=nums[i]
            if sum in dic:
                maxL=max(maxL,i-dic[sum])
            else:
                dic[sum]=i
        return maxL

s = Solution()
test = [
    {"input": [0,0,1,0,0,0,1,1], "output": 6},
    {"input": [0,1,0,1], "output":4},
    {"input": [0,1], "output":2},
]

for t in test:
    r = s.findMaxLength(t['input'])
    if r != t['output']:
        print("error:" + str(t) + " out:" + str(r))
        r = s.findMaxLength(t['input'])

