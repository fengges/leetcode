class Solution:
    def lengthOfLIS(self, nums):
        size = len(nums)
        res = [1 for n in nums]
        res.append(0)
        for i in range(1, size):
            for j in range(i):
                if nums[j] <= nums[i]:
                    res[i] = max(res[i], res[j] + 1)
        return max(res)
s=Solution()

test=[
{"input":[1,2,4,3,5,4,7,2],"output":3},
{"input":[2,2,2,2,2],"output":1},
{"input":[2,2,2,1,1,1],"output":3},
{"input":[13,0,14,7,18,18,18,16,8,15,20],"output":3},
]
for t in test:
    r=s.lengthOfLIS(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))