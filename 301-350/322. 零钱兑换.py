class Solution:
    def coinChange(self, coins, amount):
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        # print(dp)
        return dp[-1] if dp[-1] != float("inf") else -1

s = Solution()
test = [
{"input":[[227,99,328,299,42,322],9847], "output":31},
{"input":[[186,419,83,408],6249], "output":20},
]

for t in test:
    r = s.coinChange(t['input'][0],t['input'][1])
    if r != t['output']:
        print("error:" + str(t) + " out:" + str(r))