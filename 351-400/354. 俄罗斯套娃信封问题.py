class Solution:
    def maxEnvelopes(self, envelopes):
        nums=sorted(envelopes, key=lambda x:x[0])
        size = len(nums)
        res = [1 for n in nums]
        res.append(0)
        for i in range(1, size):
            for j in range(i):
                if nums[j][1] < nums[i][1] and nums[j][0] < nums[i][0]:
                    res[i] = max(res[i], res[j] + 1)
        return max(res)
s=Solution()

test=[
{"input": [[4,5],[4,6],[6,7],[2,3],[1,1]],"output":4},
{"input": [[8,3],[3,20],[15,5],[11,2],[19,6],[9,18],[1,19],[13,3],[14,20],[6,7]],"output":4},
{"input": [[2,1],[4,1],[6,2],[8,3],[10,5],[12,8],[14,13],[16,21],[18,34],[20,55]],"output":9},
{"input": [[5,4],[6,4],[6,7],[2,3]],"output":3},
]
for t in test:
    r=s.maxEnvelopes(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
