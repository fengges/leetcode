class Solution:
    def maxSlidingWindow(self, nums, k):
        res=[]
        que=[]
        for i in range(len(nums)):
            if len(que)!=0 and que[-1]<=i-k:
                que.pop()
            while len(que)!=0 and nums[que[0]]<nums[i]:
                que.pop(0)
            que.insert(0,i)
            if i>=k-1:
                res.append(nums[que[-1]])
        return res

s=Solution()
test=[

{"input":  [[1,3,-1,-3,5,3,6,7],3],"output":[3,3,5,5,6,7]},
{"input":  [[1,-1],1],"output":[1,-1]},
]

for t in test:
    r=s.maxSlidingWindow(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))