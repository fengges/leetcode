class Solution:
    def minFallingPathSum(self, A):
        r=[0 for i in A[0]]
        for line in A:
            mat=max(r)
            r.append(mat)
            r.insert(0,mat)
            tmp=[]
            for i in range(len(line)):
                tmp.append(min(r[i],r[i+1],r[i+2])+line[i])
            r=tmp
        return min(r)
s=Solution()
test=[
{"input":  [[1,2,3],[4,5,6],[7,8,9]],"output":12},
]

for t in test:
    r=s.minFallingPathSum(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))