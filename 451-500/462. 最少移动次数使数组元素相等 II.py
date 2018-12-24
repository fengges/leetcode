
class Solution:
    def minMoves2(self, nums):
        nums.sort()
        avg=nums[int(len(nums)/2)]
        res=[abs(n-avg) for n in nums ]
        return sum(res)

s=Solution()

test=[
{"input":[1,0,0,8,6],"output":14},
{"input":[1,2],"output":1},
{"input":[1,2,3],"output":2},
{"input":[-100,0,100],"output":200},
]
for t in test:
    r=s.minMoves2(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))