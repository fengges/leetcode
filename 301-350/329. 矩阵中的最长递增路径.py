class Solution:
    def add(self,dp,i1,j1,i2,j2):
        dp[i1][j1][3].append(dp[i2][j2])
        dp[i1][j1][1] = True
        dp[i2][j2][0] = True
    def longestIncreasingPath(self, matrix):
        dp=[[[False,False,0,[]] for j in i ] for i in matrix]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i+1<len(dp) and matrix[i][j]<matrix[i+1][j]:
                    self.add(dp, i, j, i + 1, j)
                elif i+1<len(dp) and matrix[i][j]>matrix[i+1][j]:
                    self.add(dp, i + 1, j, i, j)
                if j+1<len(dp[0]) and matrix[i][j]<matrix[i][j+1]:
                    self.add(dp, i, j, i, j + 1)
                elif j+1<len(dp[0]) and matrix[i][j]>matrix[i][j+1]:
                    self.add(dp, i, j + 1, i, j)
        start=[False,True,0,[]]
        end=[True,False,1,[]]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if dp[i][j][0]==False:
                    # dp[i][j][0]=True
                    start[3].append(dp[i][j])
                if dp[i][j][1]==False:
                    # dp[i][j][1]=True
                    dp[i][j][3].append(end)
        self.find(start,0)
        return end[2]-1
    def find(self,start,path):
        if path>=start[2]:
            start[2]=path
            for node in start[3]:
                self.find(node,start[2]+1)
s=Solution()
test=[
{"input":[[0,1,2,3,4,5,6,7,8,9],[19,18,17,16,15,14,13,12,11,10],[20,21,22,23,24,25,26,27,28,29],[39,38,37,36,35,34,33,32,31,30],[40,41,42,43,44,45,46,47,48,49],[59,58,57,56,55,54,53,52,51,50],[60,61,62,63,64,65,66,67,68,69],[79,78,77,76,75,74,73,72,71,70],[80,81,82,83,84,85,86,87,88,89],[99,98,97,96,95,94,93,92,91,90],[100,101,102,103,104,105,106,107,108,109],[119,118,117,116,115,114,113,112,111,110],[120,121,122,123,124,125,126,127,128,129],[139,138,137,136,135,134,133,132,131,130],[0,0,0,0,0,0,0,0,0,0]] , "output":4},
{"input":[[9,9,4],[6,6,8],[2,1,1]] , "output":4},
]
for t in test:
    r=s.longestIncreasingPath(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))