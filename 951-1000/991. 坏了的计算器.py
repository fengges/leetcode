class Solution:
    def brokenCalc(self, X, Y):
        r=0
        while X!=Y:
            if X>Y:
                r+=X-Y
                break
            elif Y%2==0:
                Y//=2
                r+=1
            else:
                Y+=1
                r+=1
        return r

s=Solution()

test=[
{"input":[2,3],"output":2},

]
for t in test:
    r=s.brokenCalc(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))