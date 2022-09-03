class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        size=len(mat)
        ans=0
        for i in range(size):
            ans+=mat[i][i]
            if 2*i+1!=size:
                ans+=mat[i][size-1-i]
        return ans