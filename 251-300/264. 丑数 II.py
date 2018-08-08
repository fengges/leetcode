class Solution:
    def nthUglyNumber(self, n):
        t=[0,0,0]
        result=[1]
        while n!=len(result):
            temp=[result[t[0]]*2,result[t[1]]*3,result[t[2]]*5]
            new=min(temp)
            result.append(new)
            for i,v in enumerate(temp):
                if v==new:
                    t[i]+=1
        return result[-1]
s=Solution()
test=[
{"input": 1432, "output":12},
{"input": 10, "output":12},
]

for t in test:
    r=s.nthUglyNumber(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.nthUglyNumber(t['input'])