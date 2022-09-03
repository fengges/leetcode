class Solution:
    def updateMatrix(self, mat) :

        col,row=len(mat[0]),len(mat)
        dp=[ [float('inf') for a in range(col+2)] for i in range(row+2) ]
        for i,m in enumerate(mat):
            for j,v in enumerate(m):
                if v==0:
                    dp[i+1][j+1]=0
                else:
                    dp[i+1][j+1]=min(dp[i+1][j],dp[i][j+1])+1
        for i,m in enumerate(mat):
            for j,v in enumerate(m):
                if mat[row-i-1][col-j-1]==0:
                    dp[row-i][col-j]=0
                else:
                    dp[row-i][col-j]=min(dp[row-i+1][col-j]+1,dp[row-i][col-j+1]+1,dp[row-i][col-j])
        return [ d[1:-1] for d in dp[1:-1] ]

s=Solution()

test=[
    {"input":[[0,0,0],[0,1,0],[1,1,1]],"output":[[0,0,0],[0,1,0],[1,1,1]]},

]
for t in test:
    r=s.updateMatrix(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))