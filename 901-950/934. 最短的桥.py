class Solution:
    def find(self,A):
        for i, line in enumerate(A):
            for j, a in enumerate(line):
                if a==1:
                    return i,j
    def shortestBridge(self, A):
        flag=[[True for C in B] for B in A]
        tmp=[]
        for i, line in enumerate(A):
            for j, a in enumerate(line):
                if a==1:
                    tmp.append([i,j])
        n_tmp=tmp
        r=0
        while len(n_tmp):
            tmp=n_tmp
            n_tmp=[]
            for n in tmp:
                i,j=n[0],n[1]
                up1 = self.getNode(i - 1, j, A,flag,A[i][j])
                up2 = self.getNode(i + 1, j, A,flag,A[i][j])
                up3 = self.getNode(i, j - 1, A,flag,A[i][j])
                up4 = self.getNode(i, j + 1, A,flag,A[i][j])
                if up1:
                    n_tmp.append([i-1,j])
                if up2:
                    n_tmp.append([i+1,j])
                if up3:
                    n_tmp.append([i,j-1])
                if up4:
                    n_tmp.append([i,j+1])

        return max([max(g) for g in A])-1
    def getNode(self,i,j,grid,flag,val):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or flag[i][j] == False:
            return
        flag[i][j] = False
        if grid[i][j]==0:
            grid[i][j]=val+1
        return grid[i][j]

s=Solution()
test=[
{"input": [[0,1,0,0,0],[0,1,0,1,1],[0,0,0,0,1],[0,0,0,0,0],[0,0,0,0,0]], "output":1},
{"input": [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]], "output":1},
]

for t in test:
    r=s.shortestBridge(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))

