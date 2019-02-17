class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        result=0
        end,size=0,len(nums)
        mul=1
        for i in range(size):
            mul*=nums[i]
            while mul >= k and end <= i:
                mul /= nums[end]
                end+=1
            result += i - end + 1
        return result



s=Solution()
test=[
{"input": [ [10,5,2,6],100], "output":8},
{"input": [ [1,1,1],100], "output":6},
]

for t in test:
    r=s.numSubarrayProductLessThanK(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))