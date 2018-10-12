class Solution:
    def maxProfit(self, prices):
        n=len(prices)
        if n==0:
            return 0
        i=1
        r=0
        while i!=n:
            d=prices[i]-prices[i-1]
            if d>0:
                r+=d
        return r