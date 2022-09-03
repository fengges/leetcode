class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        tmp=set()

        def fun(strs,ans):

            if strs in tmp:
                return strs
            tmp.add(strs)
            a1=[(int(t)+a)%10  if i%2==1 else int(t) for i,t in enumerate(strs)]
            a1=fun(''.join([str(t) for t in a1]),ans)

            a2=strs[-b:]+strs[:-b]
            a2=fun(a2,ans)

            ans=min([ans,a1,a2])

            return ans

        return fun(s,s)


s=Solution()
null=None
test=[
    {"input":121,"output":True},
    {"input":2,"output":False},
    {"input":4,"output":True},
    {"input":12,"output":False},
    {"input":81,"output":False},

]
for t in test:
    r=s.isThree(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
