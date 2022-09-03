class Solution:
    def numWays(self, n: int) -> int:
        ans=[0 for i in range(n+1)]
        ans[1]=1
        ans[2]=2
        for i in range(3,n+1):
            ans[i]=ans[i-1]+ans[i-2]
            ans[i]=ans[i]%(1e9+7)
        return ans[-1]
