class Solution:
    def removeDuplicates(self, nums):
        left=0
        num=0
        if len(nums)==0:
            return 0
        temp=nums[0]
        for i in range(len(nums)):
            if nums[i]==temp and num==2:
                continue
            elif nums[i]==temp:
                nums[left] = nums[i]
                left+=1
                num+=1
            else:
                num=1
                nums[left]=nums[i]
                left += 1
                temp=nums[i]

        return left

s=Solution()

test=[
{"input":[0,0,1,1,1,1,2,3,3],"output":2},
{"input":[1,2],"output":2},
{"input":[0,0,1,1,1,1,2,3,3],"output":7},
{"input":[1,1,1,2,2,3],"output":5},

]
for t in test:
    r=s.removeDuplicates(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.removeDuplicates(t['input'])