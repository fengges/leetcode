class Solution(object):
    def carFleet(self, target, position, speed):
        size=len(position)
        if size<=1:
            return size
        dic={k:v for k,v in enumerate(position)}
        result=sorted(dic.items(), key=lambda x:x[1],reverse=True)
        time=[(target-item[1]+0.0)/speed[item[0]] for item in result]
        m=time[0]
        r=1
        for i in range(size-1):
            if time[i+1]>m:
                r+=1
                m=time[i+1]
        return r
s=Solution()
test=[
{"input": [10,[0,4,2],[2,1,3]], "output":1},
{"input": [10,[6,8],[3,2]], "output":2},
]

for t in test:
    r=s.carFleet(t['input'][0],t['input'][1],t['input'][2])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
