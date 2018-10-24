class Solution:
    def surfaceArea(self, grid):
        r=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]>0:
                    r+=2
                    t=grid[i][j]-self.find(grid,i,j-1)
                    if t>0:
                        r+=t
                    t=grid[i][j]-self.find(grid,i,j+1)
                    if t>0:
                        r+=t
                    t=grid[i][j]-self.find(grid,i-1,j)
                    if t>0:
                        r+=t
                    t=grid[i][j]-self.find(grid,i+1,j)
                    if t>0:
                        r+=t
        return r
    def find(self,grid,i,j):
        if i<0 or j<0:
            return 0
        if i>=len(grid) or j>=len(grid[0]):
            return 0
        return grid[i][j]