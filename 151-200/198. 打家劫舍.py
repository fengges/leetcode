class Solution:
    def rob(self, nums):
        flag=[0 for i in range(len(nums)+2)]
        for i in range(len(nums)):
            flag[i+2]=max(flag[i]+nums[i],flag[i+1])
        return flag[-1]
        # return self.find(0,nums)
    def find(self,s,nums):
        if s>=len(nums):
            return 0
        return max(self.find(s+2,nums)+nums[s],self.find(s+1,nums))

s=Solution()
test=[
{"input":[183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211], "output":2},

]
for t in test:
    r=s.rob(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))