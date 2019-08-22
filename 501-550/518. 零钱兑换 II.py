class Solution:
    def change(self, amount, coins):
        dp=[0 for i in range(amount+1)]
        dp[0]=1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]


s=Solution()
test=[
{"input":[5, [1, 2, 5]] , "output":4},
]
for t in test:
    r=s.change(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))