class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        dp=[ [a for a in g] for g in grid]
        a,b=len(grid),len(grid[0])
        for j in range(1,b):
            dp[0][j]=dp[0][j-1]+grid[0][j]
        for i in range(1,a):
            dp[i][0]=dp[i-1][0]+grid[i][0]
            for j in range(1,b):
                dp[i][j]=max(dp[i][j-1],dp[i-1][j])+grid[i][j]
        return dp[-1][-1]