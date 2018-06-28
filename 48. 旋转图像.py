
class Solution:
    def rotate(self, matrix):
        length = len(matrix)
        for  i in range(length):
            for j in range(i+1,length):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]


        len2 = int(length / 2);
        for i in range(length):
            for j in range(len2):
                matrix[i][j], matrix[i][length - 1 - j]=matrix[i][length - 1 - j],matrix[i][j]
        return matrix


s=Solution()
test=[

{"input": [
  [1,2,3],
  [4,5,6],
  [7,8,9]
], "output":[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]},
{"input": [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
] , "output": [
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]},


]

for t in test:
    r=s.rotate(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.rotate(t['input'])
