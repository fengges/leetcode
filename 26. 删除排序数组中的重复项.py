class Solution:
    def removeDuplicates(self, nums):
        i=0
        if len(nums)==0:
            return 0
        for j in range(1,len(nums)):
            if nums[j]!=nums[i]:
                nums[i+1]=nums[j]
                i+=1
        return i+1

s=Solution()

test=[
{"input": [1,1,2],"output":2},
{"input": [],"output":0},
{"input": [0,0,1,1,1,2,2,3,3,4],"output":5},
      ]

for t in test:
    r=s.removeDuplicates(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.removeDuplicates(t['input'])