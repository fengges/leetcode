class Solution:
    def numDistinct(self, s, t):
        dp=[ [0 for i in range(len(s)+1)] for j in range(len(t)+1)]
        dp[0]=[1 for i in range(len(s)+1)]
        for i in range(len(t)):
            for j in range(len(s)):
                dp[i+1][j+1]=dp[i+1][j]
                if t[i]==s[j]:
                    dp[i + 1][j + 1] += dp[i][j]
        return dp[-1][-1]