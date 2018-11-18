
class Solution:
    def minCut(self, s):
        dp=[[False for i in s] for j in s]
        size=len(s)
        for i in range(size):
            dp[i][i]=True
        for i in range(size-1):
            if s[i+1]==s[i]:
                dp[i][i+1]=True
        for i in range(2,size+1):
            for j in range(size-i):
                dp[j][j+i]= dp[j+1][i+j-1] and s[i+j]==s[j]
        flag=[0 for i in range(size)]
        for i in range(1,size):
            if dp[0][i]:
                flag[i]=0
            else:
                flag[i]=flag[i-1]+1
                for j in range(1,i+1):
                    if dp[j][i]:
                        flag[i]=min(flag[i],flag[j-1]+1)
        return flag[-1]


s=Solution()
test=[
{"input":"ababababababababababababcbabababababababababababa", "output":1},
{"input":"aab", "output":1},
]
for t in test:
    r=s.minCut(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
