class Solution:
    def diagonalSum(self, mat):
        size=len(mat)
        r=0
        for i in range(size):
            r+=mat[i][i]+mat[i][size-1-i]
        if size%2==1:
            size//=2
            r-=mat[size][size]
        return r

s=Solution()
null=None
test=[
{"input": [[1,2,3],
            [4,5,6],
            [7,8,9]],"output":25},
{"input": [[1,1,1,1],
            [1,1,1,1],
            [1,1,1,1],
            [1,1,1,1]],"output":8},
{"input":[[5]],"output":5},
]
for t in test:
    r=s.diagonalSum(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))