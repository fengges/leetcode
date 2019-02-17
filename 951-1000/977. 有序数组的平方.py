class Solution:
    def sortedSquares(self, A):
        A.sort(key=lambda x:abs(x))
        return [a*a for a in A]