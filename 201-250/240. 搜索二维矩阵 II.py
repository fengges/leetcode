class Solution:
    def searchMatrix(self, matrix, target):
        i,j=len(matrix)-1,0
        while i>=0 and j<len(matrix[0]):
            if matrix[i][j]>target:
                i-=1
            elif  matrix[i][j]==target:
                return True
            else:
                j+=1
        return False

s=Solution()
test=[
{"input":[[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
],5], "output":True},
{"input":[[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
],20], "output":False},
]

for t in test:
    r=s.searchMatrix(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
