class Solution(object):
    def maxProfit(self, prices):

        if len(prices) <= 1:
            return 0

        if len(prices) == 2:
            count = prices[1] - prices[0]
            return count if count > 0 else 0

        n = len(prices)
        dp1 = [0] * n
        dp2 = [0] * n
        dp2[0] = - prices[0]

        for i in range(1, n):
            dp1[i] = max(dp1[i - 1], dp2[i - 1] + prices[i])
            temp = 0
            if i >= 2:
                temp = dp1[i - 2]
            dp2[i] = max(dp2[i - 1], temp - prices[i])

        return max(dp1[n - 1], dp2[n - 1])