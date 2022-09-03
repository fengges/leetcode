class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        a,b=len(grid),len(grid[0])
        ans=[]
        for g in grid:
            ans.extend(g)
        ans=ans[k:]+ans[:k]
        for i in range(a):
            for j in range(b):
                grid[i][j]=ans[i*b+j]
        return grid