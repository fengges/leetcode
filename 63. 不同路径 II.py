class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
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
{"input":[[1]],"output":0},
{"input":[[0,1]],"output":0},
{"input":[[0]
],"output":1},
{"input":[
  [0,0,0],
  [0,1,0],
  [0,0,0]
],"output":2},

]

for t in test:
    r=s.uniquePathsWithObstacles(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.uniquePathsWithObstacles(t['input'])
