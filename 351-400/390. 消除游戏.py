class Solution:
    def lastRemaining(self, n):
        nums=[i+1 for i in range(n)]
        left=True
        odd=1
        while len(nums)>1:
            nums=nums[::2]
        return nums[0]
s=Solution()

test=[
{"input": 10000000,"output": 6006},
{"input": 8997,"output": 6006},
{"input": 9,"output": 6},
]
for t in test:
    r=s.lastRemaining(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))