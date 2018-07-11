class Solution:
    def totalNQueens(self, n):
        self.result = 0
        queen = [None for i in range(n)]
        self.queen(queen, 0)

        return self.result

    def queen(self, A, cur=0):
        if cur == len(A):
            self.result+=1
            return
        for col in range(len(A)):
            A[cur], flag = col, True
            for row in range(cur):
                if A[row] == col or abs(col - A[row]) == cur - row:
                    flag = False
                    break
            if flag:
                self.queen(A, cur + 1)

s = Solution()

test = [
    {"input":4, "output":2}
]

for t in test:
    r = s.totalNQueens(t['input'])
    if r != t['output']:
        print("error:" + str(t) + " out:" + str(r))
        r = s.totalNQueens(t['input'])
