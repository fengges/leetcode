class Solution(object):
    def wiggleSort(self, nums):
        nums.sort()
        size=len(nums)
        length=int(size/2)
        for i in range(length):
            tmp=nums[size-length+i]
            del nums[size-length+i]
            nums.insert(2*i+1,tmp)
        return nums
s=Solution()
test=[
{"input":[1, 5, 1, 1, 6, 4], "output":[1, 4, 1, 5, 1, 6]},
]

for t in test:
    r=s.wiggleSort(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))