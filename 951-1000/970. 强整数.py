class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) :
        def func(x,bound):
            if x==1:
                return [i+1 for i in range(x)]
            ans1=1
            tmp=[]
            while ans1<=bound:
                tmp.append(ans1)
                ans1*=x
            return tmp
        tmp=func(x,bound)
        tmp2=func(y,bound)
        ans=set()
        for a in tmp:
            for a2 in tmp2:
                if a+a2<=bound:
                    ans.add(a+a2)
        return list(ans)
s=Solution()
null=None
test=[
{"input": [2,1,10],"output":[2,4,6,8,10,14]},
{"input": [2,3,10],"output":[2,4,6,8,10,14]},
{"input": [3,5,15],"output":[2,4,6,8,10,14]},
]
for t in test:
    r=s.powerfulIntegers(t['input'][0],t['input'][1],t['input'][2])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))


