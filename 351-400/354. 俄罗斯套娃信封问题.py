class Solution:
    def maxEnvelopes(self, envelopes):
        if len(envelopes)==0:
            return 0
        nums=sorted(envelopes, key=lambda x:x[0])
        size = len(nums)
        res = []
        for i in range(size):
            for r in res:
                if r[0]<nums[i][0] and r[1]<nums[i][1]:
                    res.append([nums[i][0], nums[i][1], r[2]+1])
            res.append([nums[i][0],nums[i][1],1])
        return max([r[2] for r in res])
s=Solution()

test=[
{"input": [[8,3],[3,20],[15,5],[11,2],[19,6],[9,18],[1,19],[13,3],[14,20],[6,7]],"output":4},
{"input": [[4,5],[4,6],[6,7],[2,3],[1,1]],"output":4},

{"input": [[2,1],[4,1],[6,2],[8,3],[10,5],[12,8],[14,13],[16,21],[18,34],[20,55]],"output":9},
{"input": [[5,4],[6,4],[6,7],[2,3]],"output":3},
]
for t in test:
    r=s.maxEnvelopes(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
