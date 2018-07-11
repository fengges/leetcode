class Solution:
    def sortColors(self, nums):
        left,right=0,len(nums)-1
        index=0
        while index<=right:
            if nums[index]==0:
                nums[index],nums[left]=nums[left],nums[index]
                left+=1
                index+=1
            elif nums[index]==2:
                nums[index],nums[right]=nums[right],nums[index]
                right-=1
            else:
                index+=1
        return nums

s=Solution()

test=[
{"input":[2,0,2,1,1,0],"output":[0,0,1,1,2,2]},
{"input":[1,2,0],"output":[0,1,2]},
{"input":[2,0,1],"output":[0,1,2]},

]
for t in test:
    r=s.sortColors(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.sortColors(t['input'])