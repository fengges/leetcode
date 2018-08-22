class Solution:
    def summaryRanges(self, nums):
        start=0
        result=[]
        for i in range(len(nums)-1):
            if nums[i+1]-1!=nums[i]:
                if i==start:
                    result.append(str(nums[i]))
                else:
                    result.append(str(nums[start])+'->'+str(nums[i]))
                start=i+1
        if len(nums)==0:
            return result
        elif len(nums)==1:
            return [str(nums[0])]
        elif nums[-1]-1==nums[-2]:
            result.append(str(nums[start]) + '->' + str(nums[-1]))
        else:
            result.append(str(nums[-1]))
        return result

s=Solution()
test=[
{"input": [0,1,2,4,5,7], "output":["0->2","4->5","7"]},
{"input": [0,2,3,4,6,8,9], "output":["0","2->4","6","8->9"]},
]

for t in test:
    r=s.summaryRanges(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.summaryRanges(t['input'])