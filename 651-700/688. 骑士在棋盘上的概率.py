class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp=[ [[0 for i in range(n)] for j in range(n)] for k in range(k+1)]
        dp[0][row][column]=1

        step=[ [-1,-2],[-2,-1],[-2,1],[-1,2],[1,-2],[2,-1],[2,1],[1,2] ]
        for st in range(k):
            for  i in range(n):
                for j in range(n):
                    for s in step:
                        r,c=i+s[0],j+s[1]
                        if r<0 or c<0 or r>=n or c>=n:
                            continue
                        dp[st+1][r][c]+=(dp[st][i][j])/8
        return sum([sum(a) for a in dp[k]])

s=Solution()

test=[
    {"input":[3,2,0,0],"output":2},

]
for t in test:
    r=s.knightProbability(*t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))