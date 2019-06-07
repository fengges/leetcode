class Solution:
    def orangesRotting(self, grid):
        r=0
        tmps=self.find(grid,2)
        if not tmps:
            result = self.find(grid, 1)
            return 0 if len(result) == 0 else -1
        while tmps:
            r+=1
            result = []
            for tmp in tmps:
                if self.check(grid,tmp[0]-1,tmp[1]):
                    grid[tmp[0]-1][tmp[1]]=2
                    result.append([tmp[0]-1,tmp[1]])
                if self.check(grid,tmp[0]+1,tmp[1]):
                    grid[tmp[0]+1][tmp[1]]=2
                    result.append([tmp[0] + 1, tmp[1]])

                if self.check(grid,tmp[0],tmp[1]-1):
                    grid[tmp[0]][tmp[1]-1]=2
                    result.append([tmp[0], tmp[1]-1])
                if self.check(grid,tmp[0],tmp[1]+1):
                    grid[tmp[0]][tmp[1]+1]=2
                    result.append([tmp[0], tmp[1]+1])
            tmps=result


        result = self.find(grid, 1)
        return r-1 if len(result)==0 else -1
    def check(self,grid,i,j):
        if i>=0 and i<len(grid) and j>=0 and j<len(grid[0]) and grid[i][j]==1:
            return True
        else:
            return False

    def find(self,grid,flag):
        r=[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==flag:
                    r.append([i,j])
        return r
s=Solution()
test=[
{"input":
[[2,1,1],[1,1,0],[0,1,1]],'output':4},
{"input":[[2,1,1],[1,1,0],[0,1,1]],'output':4},
]
for t in test:
    r=s.orangesRotting(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))