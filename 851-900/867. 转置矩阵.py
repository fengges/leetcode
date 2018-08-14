class Solution:
    def transpose(self, A):
        t=[ [0 for i in range(len(A))] for j in range(len(A[0]))]
        for i in range(len(A)):
            for j in range(len(A[i])):
                t[j][i]=A[i][j]
        return t

s=Solution()
test=[

{"input":[[1,2,3],[4,5,6],[7,8,9]], "output":[[1,4,7],[2,5,8],[3,6,9]]},
{"input":[[1,2,3],[4,5,6]], "output":[[1,4],[2,5],[3,6]]},
]

for t in test:
    r=s.transpose(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.transpose(t['input'])