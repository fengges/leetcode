class Solution:
    def calculateMinimumHP(self, dungeon):
        m, n= len(dungeon),len(dungeon[0])
        dp=[ [0 for l in line] for line in dungeon]
        if dungeon[m - 1][n - 1] < 0:
            dp[m - 1][n - 1] =  -1 * dungeon[m - 1][n - 1] + 1
        else:
            dp[m - 1][n - 1] =  1
        for  i in range(m-2,-1,-1):
            dp[i][n-1] = max(dp[i+1][n-1] - dungeon[i][n-1], 1)
        for i in range(n-2,-1,-1):
            dp[m-1][i] = max(dp[m-1][i+1] - dungeon[m-1][i], 1)

        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                tempMin = min(dp[i][j+1]-dungeon[i][j], dp[i+1][j]-dungeon[i][j])
                dp[i][j] = max(1, tempMin)
        return dp[0][0]
