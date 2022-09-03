class Solution:
    def uniquePathsIII(self, grid) -> int:
        size=0
        for x,g in enumerate(grid):
            for y,i in enumerate(g):
                if i==0:
                    size+=1
                elif i==1:
                    x1,y1=x,y

        flag=[ [True for i in g] for g in grid]
        step=[ [-1,0] , [1,0] , [0,-1] , [0,1] ]
        a,b=len(grid),len(grid[0])

        def dps(x,y,s):
            ans=0
            if grid[x][y]==2 and s==0:
                return 1

            for st in step:
                x1,y1=x+st[0],y+st[1]
                if x1<0 or y1<0 or x1>=a or y1>=b:
                    continue
                if flag[x1][y1] and (grid[x1][y1]==0 or grid[x1][y1]==2):
                    flag[x1][y1]=False
                    t=dps(x1,y1,s-1)
                    ans+=t
                    flag[x1][y1]=True
            return ans
        return dps(x1,y1,size+1)
s=Solution()

test=[
    {"input": [[1,0,0,0],[0,0,0,0],[0,0,2,-1]],"output":2},

]
for t in test:
    r=s.uniquePathsIII(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))