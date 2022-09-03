class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tmp=float('-inf')
        ans=float('-inf')
        for p in prices:

            tmp=min(p,tmp)
            ans=max(p-tmp,ans)
        return ans