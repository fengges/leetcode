class Solution:
    def majorityElement(self, nums):
        dic={}
        size=int(len(nums)/3)
        for n in nums:
            if n not in dic:
                dic[n]=0
            dic[n]+=1
        max=[]
        for k in dic:
            if dic[k]>size:
                max.append(k)
        return max

s=Solution()
test=[
{"input": [3,2,3], "output":[3]},
]

for t in test:
    r=s.majorityElement(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.majorityElement(t['input'])