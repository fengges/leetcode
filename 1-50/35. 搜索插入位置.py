class Solution:
    def getIndex(self,nums,target):
        left=0
        right=len(nums)-1
        isleft=True
        while left<=right:
            min=int((left+right)/2)
            if nums[min]==target:
                return min
            elif nums[min]>target:
                isleft = False
                right = min - 1
            else:
                isleft=True
                left = min + 1
        if isleft:
            return left
        else:
            return right+1
    def searchInsert(self, nums, target):
        index=self.getIndex(nums,target)

        return index

s=Solution()

test=[
{"input":[ [1,3],2],"output":1},
{"input":[ [1,3,5,6],5],"output":2},
{"input":[ [1,3,5,6],2],"output":1},
{"input":[ [1,3,5,6],7],"output":4},
{"input":[[1,3,5,6],0],"output":0},
      ]

for t in test:
    r=s.searchInsert(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.searchInsert(t['input'][0],t['input'][1])
