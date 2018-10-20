class Solution:
    def gameOfLife(self, board):
        tmp=[[0 for i in range(len(board[0])+2)] for j in range(len(board)+2)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                tmp[i+1][j+1]=board[i][j]
        for i in range(len(board)):
            for j in range(len(board[0])):
                num=self.find(tmp,i+1,j+1)
                if board[i][j]==1 and (num<2 or num>3):
                    board[i][j]=0
                elif board[i][j]==0 and num==3:
                    board[i][j]=1


    def find(self,tmp,i,j):
        return sum([tmp[i-1][j-1],tmp[i-1][j],tmp[i-1][j+1],tmp[i][j-1],tmp[i][j+1],tmp[i+1][j-1],tmp[i+1][j],tmp[i+1][j+1]])
s=Solution()
test=[
{"input":[[0,1,0],[0,0,1],[1,1,1],[0,0,0]], "output":26},
]

for t in test:
    r=s.gameOfLife(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))