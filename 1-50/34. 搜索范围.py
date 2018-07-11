class Solution:
    def getIndex(self,nums,target):
        left=0
        right=len(nums)-1
        while left<=right:
            min=int((left+right)/2)
            if nums[min]==target:
                return min
            elif nums[min]>target:
                right = min - 1
            else:
                left = min + 1
        return -1
    def searchRange(self, nums, target):
        index=self.getIndex(nums,target)
        if index==-1:
            return [-1,-1]
        else:
            s=index
            e=index
            while s>=0:
                if nums[s]==target:
                    s-=1
                else:
                    break
            while e<len(nums):
                if nums[e]==target:
                    e+=1
                else:
                    break
            return [s+1,e-1]

s=Solution()

test=[
{"input":[ [5,7,7,8,8,10],8],"output":[3,4]},
{"input":[ [1],1],"output":[0,0]},
{"input":[ [1,3],1],"output":[0,0]},
{"input":[[5,7,7,8,8,10],6],"output":[-1,-1]},

      ]

for t in test:
    r=s.searchRange(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.searchRange(t['input'][0],t['input'][1])


