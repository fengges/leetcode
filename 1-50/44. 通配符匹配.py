class Solution:
    def isMatch(self, s, p):
        lenp=len(p)
        lens=len(s)
        d=[False]*(lenp+1)
        # dp=[d]*(lens+1)
        dp=[d]
        import copy
        for i in range(lens):
            dp.append(copy.copy(d))
        dp[0][0] = True
        for i in range(lenp):
            if (p[i] == '*'):
                dp[0][i+1] = dp[0][i]
        for i in range(lens):
            for j in range(lenp):
                if (p[j] != '*') :
                    if p[j]==s[i] or p[j]=='?':
                        dp[i+1][j+1] = dp[i][j]

                else:
                    dp[i+1][j+1] = (dp[i+1][j] or dp[i][j+1] or dp[i][j])

        return dp[lens][lenp]

    def isMatch2(self,s, p):
        lenp=len(p)
        lens=len(s)
        d = [False] * (lenp + 1)
        # dp=[d]*(lens+1)
        dp = [d]
        import copy
        for i in range(lens):
            dp.append(copy.copy(d))
        dp[0][0] = True
        for j in range(1,lenp+1):
            if (p[j-1] == '*') :
                dp[0][j] = dp[0][j-1]
        for i in range(1,lens+1):
            for j in range(1, lenp + 1):
                if p[j-1] != '*':
                    if p[j-1] == s[i-1] or p[j-1] == '?':
                        dp[i][j] = dp[i - 1][j - 1];

                else:
                    dp[i][j] = dp[i-1][j] or dp[i][j-1] or dp[i-1][j-1];
        return dp[s.size()][p.size()];

s=Solution()
test=[

{"input": ("aab","c*a*b"), "output": False},
{"input": ("adceb","*a*b"), "output": True},
{"input": ("aa","a"), "output": False},
{"input": ("aa","*"), "output":True},
{"input": ("cb","?a"), "output": False},
{"input": ("acdcb","a*c?b"), "output": False},

]

for t in test:
    r=s.isMatch(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.isMatch(t['input'][0], t['input'][1])