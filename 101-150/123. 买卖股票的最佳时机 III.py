class Solution:
    def maxProfit(self, prices):
        b1,b2=-10000000,-10000000
        s1,s2 = 0,0
        for i in range(len(prices)):
            b1=max(b1, -prices[i])
            s1=max(s1, b1+prices[i])
            b2=max(b2, s1-prices[i])
            s2=max(s2, b2+prices[i])
        return s2