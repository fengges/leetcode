class NumMatrix:
    def __init__(self, matrix):
        self.matrix=matrix

    def sumRegion(self, row1, col1, row2, col2):
        return sum([sum(line[col1:col2+1])   for line in self.matrix[row1:row2+1]])

matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
print([line[2:4+1]   for line in matrix[1:3+1]])