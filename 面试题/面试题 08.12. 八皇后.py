import  copy,math
class Solution:
    def solveNQueens(self, n):
        self.result=[]
        queen=[None for i in range(n)]
        self.queen(queen,0)

        return self.result

    def queen(self,A, cur=0):
        if cur == len(A):
            temp = ['.' for i in range(cur)]
            re = [copy.deepcopy(temp) for i in range(cur)]
            for i,v in enumerate(A):
                re[i][v] = "Q"
            t=[''.join(r) for r in re]
            self.result.append(t)
            return 0
        for col in range(len(A)):
            A[cur], flag = col, True
            for row in range(cur):
                if A[row] == col or abs(col - A[row]) == cur - row:
                    flag = False
                    break
            if flag:
                self.queen(A, cur + 1)