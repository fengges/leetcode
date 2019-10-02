class Solution:
    def integerReplacement(self, n):
        dp={0:0,1:1}
        def func(n,dp):
            if n in dp:
                return dp[n]
            if n%2==0:
                ans=func(n//2,dp)
            else:
                ans=min(func(n-1,dp),func(n+1,dp))
            dp[n]=ans+1
            return dp[n]
        return func(n,dp)-1
s=Solution()

test=[
{"input":7,"output":4},
{"input":8,"output":3},

]

for t in test:
    r=s.integerReplacement(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
