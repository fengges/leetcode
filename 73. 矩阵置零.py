class Solution:
    def setZeroes(self, matrix):
        r = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    r.append([i,j])

        for t in r:
            i=t[0]
            j=t[1]
            for ro in matrix:
                ro[j]=0
            for x in range(len(matrix[0])):
                matrix[i][x]=0

        return matrix
s=Solution()

test=[
{"input":[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
],"output":[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]},
{"input":[
  [1,1,1],
  [1,0,1],
  [1,1,1]
],"output":[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]},

]
for t in test:
    r=s.setZeroes(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.setZeroes(t['input'])