class Solution:
    def removeElement(self, nums, val):
        i=0
        if len(nums)==0:
            return 0
        for j in range(0,len(nums)):
            if nums[j]!=val:
                nums[i+1]=nums[j]
                i+=1
        return i


s=Solution()

test=[
{"input": [[3,2,2,3],3],"output":2},
{"input":[[0,1,2,2,3,0,4,2],2],"output":5},
      ]

for t in test:
    r=s.removeElement(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.removeElement(t['input'][0],t['input'][1])