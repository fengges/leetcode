class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):

        w,h=len(obstacleGrid),len(obstacleGrid[0])
        path=[ [ 0 for c in line ] for line in obstacleGrid]
        for i in range(w):
            for j in range(h):
                if obstacleGrid[i][j]==0:
                    if i==0 and j==0:
                        path[0][0]=1
                    elif i==0:
                        path[0][j]= path[0][j-1]
                    elif j==0:
                        path[i][0]= path[i-1][0]
                    else:
                        path[i][j]= path[i-1][j]+ path[i][j-1]
        return path[w-1][h-1]
    def uniquePathsWithObstacles2(self, obstacleGrid):
        if obstacleGrid[0][0]==1:
            return 0
        w,h=len(obstacleGrid),len(obstacleGrid[0])
        list=[[0,0]]
        num=0
        while len(list)>0:
            temp=list[0]
            if temp[0]==w-1 and temp[1]==h-1 and obstacleGrid[temp[0]][temp[1]]==0:
                num+=1
            del list[0]
            if temp[0]<w-1 and obstacleGrid[temp[0]+1][temp[1]]==0:
                list.append([temp[0]+1,temp[1]])
            if temp[1]<h-1 and obstacleGrid[temp[0]][temp[1]+1]==0:
                list.append([temp[0],temp[1]+1])


        return num
s=Solution()

test=[
{"input":[
  [0,0,0],
  [0,1,0],
  [0,0,0]
],"output":2},
{"input":[[1]],"output":0},
{"input":[[0,1]],"output":0},
{"input":[[0]
],"output":1},


]

for t in test:
    r=s.uniquePathsWithObstacles(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.uniquePathsWithObstacles(t['input'])
