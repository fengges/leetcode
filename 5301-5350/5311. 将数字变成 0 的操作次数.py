class Solution:
    def numberOfSteps (self, num: int):
        if num==0:
            return 0
        return self.numberOfSteps(num-1)+1 if num%2==1 else self.numberOfSteps(num//2)+1

s=Solution()
null=None
test=[
{"input": 14,"output":6},
{"input":8,"output":4},
{"input":123,"output":12},
]
for t in test:
    r=s.numberOfSteps(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))

