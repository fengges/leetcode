class Solution:
    def reachNumber(self, target):
        sum=0
        step=0
        now=1
        target=abs(target)
        while True:
            sum+=now
            now+=1
            step+=1
            if sum==target:
                return step
            elif sum>target:
                if (sum-target)%2==0:
                    return step

s=Solution()
test=[
{"input": 2, "output":3},
]

for t in test:
    r=s.reachNumber(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))