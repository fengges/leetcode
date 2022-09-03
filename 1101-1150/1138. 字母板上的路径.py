class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z0000"]
        a,b=len(board),len(board[1])

        index={board[i][j]:[i,j] for j in range(b) for i in range(a)}
        ans=''
        x,y=0,0
        for a in target:
            t=a
            if t=='z':
                t='u'
                ans+='U'

            i=index[t]
            if i[0]>x:
                ans+='D'*(i[0]-x)
            elif i[1]<x:
                ans+='U'*(x-i[0])
            if i[1]>y:
                ans+='R'*(i[1]-y)
            elif i[1]<y:
                ans+='L'*(y-i[1])

            ans+='!'
            x,y=i[0],i[1]
        return ans
