class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        ans=[]
        for m in matrix:
            ans.extend(m)

        return target in ans