class Solution:
    def getValidSudoku(self,y,x, board):
        result=[True for i in range(0,10)]
        t=board[y][x]
        # line
        line=board[y]
        for i in range(len(line)):
            if line[i]!='.' :
                result[int(line[i])]=False
        # column
        column = [l[x] for l in board]
        for i in range(len(column)):
            if column[i] !='.':
                result[int(column[i])] = False

        for i in range(int(x / 3) * 3,int( x / 3) * 3+3):
            for j in range(int(y / 3) * 3,int(y / 3) * 3+3):
                if board[j][i]!='.':
                    result[int(board[j][i])] = False
        return result
    def solve(self,m):
        if m==81 or len(self.result)!=0:
            import  copy
            self.result = copy.copy(self.board)
            return True
        x,y = int(m / 9),m % 9
        t=self.board[y][x]
        if t=='.':
            r=self.getValidSudoku(y,x,self.board)
            for i in range(1,10):
                if r[i]:
                    self.board[y][x]=str(i)
                    temp=self.solve(m + 1)
                    if temp:
                        return True
                    self.board[y][x] = '.'
            return False
        else:
            return self.solve(m+1)

    def solveSudoku(self, board):
        self.board=board
        self.result=[]
        self.solve(0)


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
    r=s.solveSudoku(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.solveSudoku(t['input'])
