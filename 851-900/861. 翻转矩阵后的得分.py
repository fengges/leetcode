class Solution:
    def matrixScore(self, A):
        for line in A:
            if line[0]==0:
                for i in range(len(line)):
                    line[i]=1-line[i]
        for j in range(len(A[0])):
            one=0
            for i in range(len(A)):
                if A[i][j]==1:
                    one+=1
            if len(A)-one>one:
                for i in range(len(A)):
                    A[i][j]=1-A[i][j]
        r=0
        for line in A:
            n=0
            for l in line:
                n=n*2+l
            r+=n
        return r
