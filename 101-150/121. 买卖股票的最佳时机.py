class Solution:
    def maxProfit(self, prices):
        if len(prices)==0:
            return 0
        buy=prices[0]
        result=0
        for i in range(1,len(prices)):
            buy=min(buy,prices[i])
            result=max(result,prices[i]-buy)
        return result


s=Solution()
test=[
{"input":[7,1,5,3,6,4], "output":5},
]

for t in test:
    r=s.maxProfit(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.maxProfit(t['input'])