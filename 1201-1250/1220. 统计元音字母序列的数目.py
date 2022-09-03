class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp=[[1,1,1,1,1] for i in range(n)]

        for i in range(1,n):
            dp[i][0]=(dp[i-1][1]+dp[i-1][2]+dp[i-1][4])%1000000007
            dp[i][1]=(dp[i-1][0]+dp[i-1][2])%1000000007
            dp[i][2]=(dp[i-1][1]+dp[i-1][3])%1000000007
            dp[i][3]=dp[i-1][2]
            dp[i][4]=(dp[i-1][2]+dp[i-1][3])%1000000007
        return sum(dp[-1])%1000000007


    def countVowelPermutation2(self, n: int) -> int:
        dp = (1, 1, 1, 1, 1)
        for _ in range(n - 1):
            dp = ((dp[1] + dp[2] + dp[4]) % 1000000007, (dp[0] + dp[2]) % 1000000007, (dp[1] + dp[3]) % 1000000007, dp[2], (dp[2] + dp[3]) % 1000000007)
        return sum(dp) % 1000000007

s=Solution()

test=[
    {"input":6,"output":2},


]
for t in test:
    r=s.countVowelPermutation(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))

for i in range(6,1000):
    if s.countVowelPermutation(i)!=s.countVowelPermutation2(i):
        print(i)
