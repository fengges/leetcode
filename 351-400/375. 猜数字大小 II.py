class Solution:
    def getMoneyAmount(self, n):
        def DP(ans, start , end):
            if start>=end:
                return 0
            elif ans[start][end]:
                return ans[start][end]
            else:
                ans[start][end] = float("inf")
                for i in range(start,end):
                    left=DP(ans,start,i-1)
                    right=DP(ans,i+1,end)
                    k=i+max(left,right)
                    ans[start][end]=min( ans[start][end],k)
        ans = [[0]*(n+1) for i in range(n)]
        return DP(ans,1,n)
