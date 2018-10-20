class Solution:
    def integerBreak(self, n):
        dic={}
        dic[1]=1
        dic[2]=1
        if n<=2:
            return dic[n]
        for i in range(3,n+1):
            dic[i]=0
            for j in range(1,i):
                dic[i]=max(dic[i],max(j,dic[j])*max(dic[i-j],i-j))
        return dic[n]
s=Solution()
test=[
{"input":  10, "output":36},
]

for t in test:
    r=s.integerBreak(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))