class Solution:
    def maxProfit(self, prices, fee):
        n = len(prices)
        buy = -prices[0]
        cash = 0
        for i in range(1,n):
            cash=max(cash, buy+prices[i]-fee)
            buy=max(buy, cash-prices[i])

        return cash
