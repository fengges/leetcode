class Solution:
    def cherryPickup(self, grid):
        flag=self.find(grid)
        num=flag[-1][-1]
        if num==-1:
            return 0
        i,j=len(grid),len(grid[0])
        grid[-1][-1]=0
        while not( i==1 and j==1):
            if i==1:
                j-=1
            elif j==1:
                i-=1
            elif flag[i-1][j]>=flag[i][j-1]:
                i-=1
            else:
                j-=1
            grid[i-1][j-1]=0
        return num+self.find(grid)[-1][-1]
    def find(self,grid):
        flag=[[0 for j in range(len(grid[0])+1)] for i in range(len(grid)+1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if flag[i][j+1]==-1 and flag[i+1][j]==-1:
                    flag[i + 1][j + 1] = -1
                elif grid[i][j]==-1  :
                    flag[i+1][j+1]=-1
                else:
                    flag[i+1][j+1]=max(flag[i][j+1],flag[i+1][j])+grid[i][j]
        return flag
s=Solution()

test=[
{"input":[[1,1,1,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,1],[1,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,1,1,1]],"output":15},
{"input":[[1,1,-1],[1,-1,1],[-1,1,1]],"output":0},
{"input":[[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]],"output":5},
]
for t in test:
    r=s.cherryPickup(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))

