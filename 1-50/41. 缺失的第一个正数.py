class Solution:
    def firstMissingPositive(self, nums):
        nums.append(0)
        length=len(nums)

        i=0
        while i<length:
            if nums[i]>0 and nums[i]!=i and nums[i]<length and nums[nums[i]]!=nums[i]:
                nums[nums[i]],nums[i]=nums[i],nums[nums[i]]
            else:
                i+=1
        for i in range(1,length):
            if nums[i]!=i:
                return i
        return length
    def firstMissingPositive2(self,nums):
        if len(nums)==0:
            return 1
        dic={}
        for i in nums:
            dic[i]=1
        for i in range(1,max(nums)):
            if i not in dic:
                return i
        return max(nums)+1

s=Solution()

test=[
{"input":[1],"output":2},
{"input":[3,4,-1,1],"output":2},
{"input":[1,2,0],"output":3},
{"input":[7,8,9,11,12],"output":1},
      ]

for t in test:
    r=s.firstMissingPositive2(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.firstMissingPositive(t['input'])

