class Solution:
    def fib(self, n: int) -> int:
        ans=[i for i in range(n+1)]
        for j in range(2,n+1):
            ans[j]=ans[j-1]+ans[j-2]
            ans[j]=int(ans[j]%(1e9+7))
        return ans[n]
