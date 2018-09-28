class Solution:
    def numIslands(self, grid):
        flag = [[True for c in line] for line in grid]
        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and flag[i][j] == True:
                    self.count(i,j,grid,flag)
                    area+=1
        return area

    def count(self, i, j, grid, flag):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or flag[i][j] == False or grid[i][j] == '0':
            return
        flag[i][j] = False
        self.count(i - 1, j, grid, flag)
        self.count(i, j - 1, grid, flag)
        self.count(i + 1, j, grid,flag)
        self.count(i, j + 1, grid, flag)