class Solution:
    def canJump(self, nums):
        if len(nums)<=1:
            return True
        length=0
        i=0
        index=0
        while i<len(nums):
            if i+nums[i]>=len(nums)-1:
                return True
            max=-1
            for j in range(i+1,i+nums[i]+1):
                if max<nums[j]+j:
                    index=j
                    max=nums[j]+j
            length+=1
            if i==index:
                return False
            i=index

        return length

s=Solution()

test=[
{"input":[2,3,1,1,4],"output":True},
{"input":[3,2,1,0,4],"output":False},
]

for t in test:
    r=s.canJump(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.canJump(t['input'])
