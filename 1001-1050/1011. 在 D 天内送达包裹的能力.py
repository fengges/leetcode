class Solution:
    def shipWithinDays(self, weights, days: int):
        weights.sort(reverse=True)

        ans=[0 for i in range(days)]
        for w in weights:
            index=ans.index(min(ans))
            ans[index]+=w
        return max(ans)


s=Solution()

test=[
    {"input":[[1,2,3,4,5,6,7,8,9,10],5],"output":15},

]
for t in test:
    r=s.shipWithinDays(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
