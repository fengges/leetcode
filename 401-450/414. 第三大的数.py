class Solution:
    def thirdMax(self, num):
        nums=[]
        for i in num:
            if i not in nums:
                nums.append(i)
        nums.sort()
        nums.reverse()
        if len(nums)<3:
            return nums[0]
        return nums[2]

s=Solution()

test=[

{"input":[1,2],"output": 2},
{"input":[2,2,3,1],"output":1},
]
for t in test:
    r=s.thirdMax(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.thirdMax(t['input'])
