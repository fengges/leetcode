class Solution:
    def jump(self, nums):
        if len(nums)<=1:
            return 0
        length=0
        i=0
        index=0
        while i<len(nums):
            if i+nums[i]>=len(nums)-1:
                return length+1
            max=-1
            for j in range(i+1,i+nums[i]+1):
                if max<nums[j]+j:
                    index=j
                    max=nums[j]+j
            length+=1
            i=index

        return length

s=Solution()

test=[
{"input":[3,2,1,0,4],"output":2},

]

for t in test:
    r=s.jump(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.jump(t['input'])
