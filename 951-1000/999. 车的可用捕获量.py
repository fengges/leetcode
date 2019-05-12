class Solution:
    def numRookCaptures(self, board):
        i,j=self.find(board)
        r=0
        for x in range(i+1,len(board[0])):
            if board[x][j]==".":
                continue
            else:
                if board[x][j]=="p":
                    r+=1
                break
        for x in range(i-1,-1,-1):
            if board[x][j]==".":
                continue
            else:
                if board[x][j]=="p":
                    r+=1
                break
        for y in range(j+1,len(board)):
            if board[i][y]==".":
                continue
            else:
                if board[i][y]=="p":
                    r+=1
                break
        for y in range(j-1,-1,-1):
            if board[i][y]==".":
                continue
            else:
                if board[i][y]=="p":
                    r+=1
                break
        return r
    def find(self,board):
        for i,line in enumerate(board):
            for j,p in enumerate(line):
                if p=="R":
                    return i,j
        return -1,-1

