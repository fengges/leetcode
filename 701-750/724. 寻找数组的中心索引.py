class Solution:
    def pivotIndex(self, nums):
        sum=0
        for n in nums:
            sum+=n
        l=0
        for i in range(0,len(nums)):
            if (sum-nums[i])/2==l:
                return i
            l+=nums[i]
        return -1

s=Solution()
test=[
{"input": [], "output":-1},
{"input": [-1,-1,-1,0,1,1], "output":0},
{"input": [1, 7, 3, 6, 5, 6], "output":3},
{"input": [1, 2, 3], "output":-1},
]

for t in test:
    r=s.pivotIndex(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.pivotIndex(t['input'])