class Solution:
    def maxDistance(self, grid ) -> int:
        que=[]
        ans=[ [True for a in l]  for l in grid]
        flag=[ [float('inf') for t in l] for l in grid]
        for i,line in enumerate(grid):
            for j,v in enumerate(line):
                if v==1:
                    que.append([i,j])
                    ans[i][j]=False
                    flag[i][j]=0
        if not que or len(que)==len(grid)*len(grid[0]):
            return -1

        size1,size2=len(grid),len(grid[0])
        while que:
            i,j=que.pop(0)
            if i>0 and ans[i-1][j]:
                ans[i-1][j]=False
                flag[i-1][j]=min(flag[i-1][j],flag[i][j]+1)
                que.append([i-1,j])
            if j>0 and ans[i][j-1]:
                ans[i][j-1]=False
                flag[i][j-1]=min(flag[i][j-1],flag[i][j]+1)
                que.append([i,j-1])
            if i<size1-1 and ans[i+1][j]:
                ans[i+1][j]=False
                flag[i+1][j]=min(flag[i+1][j],flag[i][j]+1)
                que.append([i+1,j])
            if j<size2-1 and ans[i][j+1]:
                ans[i][j+1]=False
                flag[i][j+1]=min(flag[i][j+1],flag[i][j]+1)
                que.append([i,j+1])
        return max([max(a) for a in flag])

s=Solution()
test=[
    {"input": [[1,0,1],[0,0,0],[1,0,1]], "output":2},


]

for t in test:
    r=s.maxDistance(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))