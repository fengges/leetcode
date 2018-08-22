class Solution:
    def dominantIndex(self, nums):
        maxIndex=0
        for i,n in enumerate(nums):
            if n>nums[maxIndex]:
                maxIndex=i
        second=0
        if maxIndex==0 and len(nums)>1:
            second=1
        for i,n in enumerate(nums):
            if n>nums[second] and i!=maxIndex:
                second=i
        if nums[maxIndex]>=nums[second]*2 or maxIndex==second:
            return maxIndex
        else:
            return -1

s=Solution()
test=[
{"input": [3,0,0,2], "output":-1},
{"input": [1], "output":0},
{"input": [0,0,0,1], "output":3},
{"input": [0,0,2,1], "output":2},
]

for t in test:
    r=s.dominantIndex(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.dominantIndex(t['input'])