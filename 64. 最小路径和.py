class Solution:
    def minPathSum(self, grid):
        w,h=len(grid),len(grid[0])
        path=[ [ 0 for c in line ] for line in grid]
        for i in range(w):
            for j in range(h):
                if i==0 and j==0:
                    path[0][0]=grid[0][0]+path[0][0]
                elif i==0:
                    path[0][j]=grid[0][j]+ path[0][j-1]
                elif j==0:
                    path[i][0]=grid[i][0]+ path[i-1][0]
                else:
                    path[i][j]=grid[i][j]+ min(path[i-1][j],path[i][j-1])
        return path[w-1][h-1]