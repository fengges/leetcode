class Solution:
    count=0
    a=[]
    def isValidSudoku(self, board):
        for y in range(len(board)):
            for x in range(len(board[y])):
                t=board[y][x]
                if t!='.':
                    # line
                    line=board[y]
                    for i in range(len(line)):
                        if line[i]==t and i!=x:
                            return False
                    # column
                    column = [l[x] for l in board]
                    for i in range(len(column)):
                        if column[i] == t and i!=y:
                            return False


                    for i in range(int(x / 3) * 3,int( x / 3) * 3+3):
                        for j in range(int(y / 3) * 3,int(y / 3) * 3+3):
                            if board[j][i]==t and (i!=x or j!=y):
                                return False
        return True
s=Solution()

test=[
{"input":[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
],"output":True},
{"input":[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
],"output":False},
      ]

for t in test:
    r=s.isValidSudoku(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.isValidSudoku(t['input'])