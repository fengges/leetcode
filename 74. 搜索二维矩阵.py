class Solution:
    def searchMatrix(self, matrix, target):
        for index,row in enumerate(matrix):
            if index!=len(matrix)-1:
                if matrix[index][0]<=target and matrix[index+1][0]>target:
                    return self.find(row,target)
            else:
                return self.find(row,target)
        return False
    def find(self,row,t):
        for value in row:
            if value==t:
                return True
        return False


s=Solution()
test=[
{"input": [ [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
],3], "output":True},
{"input": [[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
],13], "output":False},
]

for t in test:
    r=s.searchMatrix(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.searchMatrix(t['input'][0], t['input'][1])