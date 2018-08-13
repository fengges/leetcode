class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = int((left + right) / 2)
            if nums[mid] > nums[right]:
                left=mid+1
            elif nums[mid] == nums[right] :
                left+=1
            else:
                right = mid
        return nums[left]

s=Solution()
test=[
{"input": [3,3,1,3], "output":1},
{"input": [4,5,6,7,0,1,2], "output":0},
{"input": [3,4,5,1,2], "output":1},

]

for t in test:
    r=s.findMin(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.findMin(t['input'])