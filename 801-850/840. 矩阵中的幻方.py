class Solution:
    def numMagicSquaresInside(self, grid):
        def isMagic(grid):
            Ma = []
            Mi = []
            M = []
            for p in range(3):
                Ma.append(max(grid[p]))
                Mi.append(min(grid[p]))
                M.extend(grid[p])  # 记住extend的用法
            if max(Ma) > 9:  # 判断矩阵是否有大于9的值
                print('max', max(Ma))
                return 0
            if min(Mi) < 1:  # 判断矩阵是否有小于1的值
                return 0
            if len(list(set(M))) != 9:  # 判断矩阵是否有重复的数
                return 0
            x1 = grid[0][0] + grid[0][1] + grid[0][2]  # 第一行
            x2 = grid[1][0] + grid[1][1] + grid[1][2]  # 第二行
            x3 = grid[2][0] + grid[2][1] + grid[2][2]  # 第三行
            y1 = grid[0][0] + grid[1][0] + grid[2][0]  # 第一列
            y2 = grid[0][1] + grid[1][1] + grid[2][1]  # 第二列
            y3 = grid[0][2] + grid[1][2] + grid[2][2]  # 第三列
            d1 = grid[0][0] + grid[1][1] + grid[2][2]  # 对角线
            d2 = grid[0][2] + grid[1][1] + grid[2][0]  # 反对角线
            print(x1, x2, x3, y1, y2, y3, d1, d2)
            if x1 == x2 and x2 == x3 and x3 == y1 and y1 == y2 and y2 == y3 and y3 == d1 and d1 == d2:
                return 1
            else:
                return 0

        row = len(grid)
        count = 0
        colum = len(grid[0])
        if row < 3 and colum < 3:
            return 0
        for i in range(1,row - 1):
            for j in range(1,colum - 1):
                if grid[i][j]==5:
                    L1 = grid[i-1:i + 2]
                    L2 = []
                    for p in range(3):
                        L2.append(L1[p][j-1:j + 2])
                    count = count + isMagic(L2)
        return count