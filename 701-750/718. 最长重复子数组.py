class Solution:
    def findLength(self, A, B):
        result=[ [0 for i in range(len(B)+1)] for j in range(len(A)+1)]
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i]==B[j]:
                    result[i+1][j+1]=result[i][j]+1
                else:
                    result[i + 1][j + 1]=0
        r=0
        for line in result:
            for i in line:
                r=max(i,r)
        return r

s=Solution()
test=[
{"input": [[0,0,0,0,0],[0,0,0,0,0]], "output":5},
{"input": [[1,2,3,2,1],[3,2,1,4,7]], "output":3},
]

for t in test:
    r=s.findLength(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.findLength(t['input'][0], t['input'][1])