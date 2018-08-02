class Solution:
    def maxProfit(self, prices):
        minIndex=prices.index(min(prices))
        if minIndex==len(prices)-1:
            return 0
        maxIndex=prices[minIndex:].index(max(prices[minIndex:]))+ minIndex
        return prices[maxIndex]-prices[minIndex]


s=Solution()
test=[
{"input":[7,1,5,3,6,4], "output":5},
]

for t in test:
    r=s.maxProfit(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.maxProfit(t['input'])