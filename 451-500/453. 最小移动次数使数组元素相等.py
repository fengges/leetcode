class Solution:
    def minMoves(self, nums):
        return sum(nums)-min(nums)*len(nums)
s=Solution()

test=[
{"input":[1,2,3],"output":3},
{"input":[-100,0,100],"output":300},
]
for t in test:
    r=s.minMoves(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
