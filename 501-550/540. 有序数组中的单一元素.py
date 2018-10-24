class Solution(object):
    def singleNonDuplicate(self, nums):
        size=len(nums)
        if size==1:
            return nums[0]
        mid=int(len(nums)/2)
        if mid%2==0:
            if nums[mid]==nums[mid+1]:
                return self.singleNonDuplicate(nums[mid+2:])
            else:
                return self.singleNonDuplicate(nums[:mid+1])
        else:
            if nums[mid]==nums[mid-1]:
                return self.singleNonDuplicate(nums[mid+1:])
            else:
                return self.singleNonDuplicate(nums[:mid])

s=Solution()

test=[
{"input":  [3,3,7,7,10,11,11],"output":10},
{"input": [1,1,2,3,3,4,4,8,8],"output":2},

{"input": [0,1,1],"output":0},

]

for t in test:
    r=s.singleNonDuplicate(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))

