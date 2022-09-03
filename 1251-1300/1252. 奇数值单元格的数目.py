class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        dp=[[0 for i in range(n)] for j in range(m)]
        for inde in indices:
            for i in range(n):
                dp[inde[0]][i]+=1
            for j in range(m):
                dp[j][inde[1]]+=1
        return sum([ len([1 for a in d if a%2==1])  for d in dp])