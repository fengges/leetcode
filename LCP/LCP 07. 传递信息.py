class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        dp=[[0 for i in range(n)] for j in range(n)]
        for r in relation:
            dp[r[0]][r[1]]=1

        def func(index,k):
            if  k==0:
                return None
            for i in range(n):
                if dp[index][i]==1:
                    t=func(i,k-1)
                    if t:
                        return t
            return None
        return func(0,k)