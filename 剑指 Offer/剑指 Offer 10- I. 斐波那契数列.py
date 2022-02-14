class Solution:
    def fib(self, n: int) -> int:
        ans=[i for i in range(n+1)]
        for j in range(2,n+1):
            ans[j]=ans[j-1]+ans[j-2]
        return ans[n]

s=Solution()
null=None
test=[
    {"input":45,"output":True},

]
for t in test:
    r=s.fib(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))