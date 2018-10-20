class Solution:
    def validTicTacToe(self, board):
        dic={'O':-1,'X':1,' ':0}
        #统计行
        line=[sum(dic[l] for l in lines) for lines in board]
        # 统计列
        colom=[sum(dic[board[i][j]] for i in range(len(board))) for j in range(len(board[0]))]
        #统计对角线
        a,b=sum([dic[board[0][0]],dic[board[1][1]],dic[board[2][2]]]),sum([dic[board[2][0]],dic[board[1][1]],dic[board[0][2]]])
        # 统计棋子数
        num1,num2=sum([sum(1 for l in lines if l=="O") for lines in board]),sum([sum(1 for l in lines if l=="X") for lines in board])
        # 判断行列是否有三个
        l,c=[i for i in line if i==3 or i==-3] ,[i for i in colom if i==3 or i==-3]
        # 行和列，最多有一行是一样的棋子
        if len(l)>1 or len(c)>1:
            return False
        # 判断棋子数量对不对
        if not (num1==num2 or num1+1==num2):
            return False
        # X赢的时候，棋子数量不可能一直
        if num1==num2 and (sum(l)==3 or sum(c)==3 or a==3 or b==3):
            return False
        # O赢的时候，X不可能比O多一个
        if num1+1==num2 and (sum(l)==-3 or sum(c)==-3 or a==-3 or b==-3):
            return False
        return True
s=Solution()
test=[
{"input":["OXX","XOX","OXO"], "output":False},
{"input":["XXX","XOO","OO "], "output":False},
{"input":["O  ", "   ", "   "], "output":False},
{"input":["XOX", " X ", "   "], "output":False},
{"input":["XXX", "   ", "OOO"], "output":False},
{"input":["XOX", "O O", "XOX"], "output":True},
]

for t in test:
    r=s.validTicTacToe(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))