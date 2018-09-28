class Solution:
    def solve(self, board):
        if len(board)==0:
            return []
        flag=[[False for l in line] for line in board]
        list=[]
        for i in range(len(board)):
            if board[i][0]=='O':
                list.append([i,0])
        for i in range(len(board)):
            if board[i][-1] == 'O':
                list.append([i,len(board[0])-1])
        for i in range(len(board[0])):
            if board[0][i]=='O':
                list.append([0,i])
        for i in range(len(board[0])):
            if board[-1][i]=='O':
                list.append([len(board)-1,i])
        for l in list:
            self.count(l[0],l[1],board,flag)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if flag[i][j]==False:
                    board[i][j]='X'
        return board
    def count(self,i,j,grid,flag):
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or flag[i][j] or grid[i][j]=='X':
            return
        flag[i][j]=True
        self.count(i-1,j,grid,flag)
        self.count(i,j-1,grid,flag)
        self.count(i+1,j,grid,flag)
        self.count(i,j+1,grid,flag)

s = Solution()
test = [
{"input":[["O","O","O"],["O","O","O"],["O","O","O"]], "output": 6},
{"input":[["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]], "output": 6},
{"input":[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]], "output": 6},
]

for t in test:
    r = s.solve(t['input'])
    if r != t['output']:
        print("error:" + str(t) + " out:" + str(r))
        r = s.solve(t['input'])