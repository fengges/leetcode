class Solution(object):
    def wiggleSort(self, nums):
        nums.sort()
        size=len(nums)
        length=int(size/2)
        left=nums[0:size-length]
        left.reverse()
        right = nums[size-length:]
        right.reverse()
        for i in range(length):
            nums[2*i]=left[i]
            nums[2 * i+1] = right[i]
        if size%2!=0:
            nums[-1]=left[-1]
        return nums
s=Solution()
test=[
{"input":[5,3,1,2,6,7,8,5,5], "output":[5,8,5,7,3,6,2,5,1]},
{"input":[1], "output":[1]},
{"input":[4,5,5,6], "output":[5,6,4,5]},
{"input":[1, 5, 1, 1, 6, 4], "output":[1, 4, 1, 5, 1, 6]},
]

for t in test:
    r=s.wiggleSort(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))