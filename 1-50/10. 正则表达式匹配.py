class Solution:


    def isMatch(self, s, p):

        if not p :return not s
        if not s :
            if len(p)>=2 and p[1]=='*':
                return self.isMatch(s,p[2:])
            return not p
        if len(p)>=2 and p[1]=='*':
            t=self.isMatch(s,p[2:])
            if t:
                return True

            if p[0]=='.' or p[0]==s[0]:
                return self.isMatch(s[1:],p)
            else:
                return False
        else:
            if p[0]=='.' or p[0]==s[0]:
                return self.isMatch(s[1:],p[1:])
            else:
                return False
    def isMatch2(self, s, p):
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
            if (p[i] == '*' and dp[0][i-1]):
                dp[0][i+1] = True
        for i in range(lens):
            for j in range(lenp):
                if (p[j] == '.'  or p[j] == s[i]) :
                    dp[i+1][j+1] = dp[i][j]
                if (p[j] == '*') :
                    if (p[j-1] != s[i] and p[j-1] != '.') :
                        dp[i+1][j+1] = dp[i+1][j-1]
                    else :
                        dp[i+1][j+1] = (dp[i][j+1] or dp[i+1][j-1])
        return dp[lens][lenp]


s=Solution()
test=[
    {"input": ("aaa","a*a"), "output": True},
    {"input": ("aa", "a*"), "output":True},
    {"input": ("ab",".*"), "output": True},
    {"input": ("aaa","ab*a*c*a"), "output": True},
    {"input": ("ab",".*.."), "output":True},
{"input": ("a","ab*a"), "output": False},


{"input": ("","."), "output": False},
{"input": ("bbbba",".*a*a"), "output": True},
{"input": ("ab",".*c"), "output": False},
{"input": ("aab", "c*a*b"), "output": True},
{"input": ("aaa","aaaa"), "output": False},


{"input": ("aa", "a"), "output": False},

{"input":("mississippi","mis*is*p*."),"output":False},
]

for t in test:

        r=s.isMatch(t['input'][0],t['input'][1])
        if r!=t['output']:
            print("error:"+str(t)+" out:"+str(r))
            r = s.isMatch(t['input'][0], t['input'][1])
