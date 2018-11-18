class Solution:
    def rob(self, nums):
        if len(nums)==1:
            return nums[0]
        return max(self.rob2(nums[1:]),self.rob2(nums[:-1]))
    def rob2(self, nums):
        flag=[0 for i in range(len(nums)+2)]
        for i in range(len(nums)):
            flag[i+2]=max(flag[i]+nums[i],flag[i+1])
        return flag[-1]

s=Solution()
test=[
{"input":[1], "output":2},

]
for t in test:
    r=s.rob(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))