class Solution:
    def flipAndInvertImage(self, A):
        row=len(A)
        col=len(A[0])
        for i in range(row):
            for j in range(int(col/2)):
                temp=A[i][j]
                A[i][j]=A[i][col-1-j]
                A[i][col - 1 - j]=temp
        for i in range(row):
            for j in range(col):
                if A[i][j]==0:
                    A[i][j]=1
                else:
                    A[i][j]=0
        return A


s=Solution()
test=[
{"input": [[1,1,0],[1,0,1],[0,0,0]], "output":[[1,0,0],[0,1,0],[1,1,1]]},
]

for t in test:
    r=s.flipAndInvertImage(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.flipAndInvertImage(t['input'])