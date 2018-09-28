class Solution:
    def maxAreaOfIsland(self, grid):
        flag=[[True for c in line ] for line in grid]
        area=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and flag[i][j]==True:
                    n=self.count(i,j,grid,flag)
                    area=max(area,n)
        return area
    def count(self,i,j,grid,flag):
        num=0
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or flag[i][j]==False or grid[i][j]==0:
            return num
        flag[i][j]=False
        return 1+self.count(i-1,j,grid,flag)+self.count(i,j-1,grid,flag)+self.count(i+1,j,grid,flag)+self.count(i,j+1,grid,flag)

s = Solution()
test = [
{"input":[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]], "output": 6},
{"input":[[0,0,0,0,0,0,0,0]], "output": 0},
]

for t in test:
    r = s.maxAreaOfIsland(t['input'])
    if r != t['output']:
        print("error:" + str(t) + " out:" + str(r))
        r = s.maxAreaOfIsland(t['input'])

