class Solution:
    def findTargetSumWays(self, nums, S):
        self.r=0
        self.find(nums,S,0,0)
        return self.r
    def find(self,nums,s,sum,start):
        if start==len(nums):
            if sum==s:
                self.r+=1
        else:
            self.find(nums,s,sum+nums[start],start+1)
            self.find(nums,s,sum-nums[start],start+1)

s=Solution()
test=[
{"input":[[1, 1, 1, 1, 1],3], "output":5},

]
for t in test:
    r=s.findTargetSumWays(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))