class Solution:
    def candy(self, ratings):
        flag=[1 for i in ratings]
        for i in range(len(ratings)-1):
            if ratings[i+1]>ratings[i]:
                flag[i+1]=flag[i]+1
        for i in range(len(ratings)-1,0,-1):
            if ratings[i-1]>ratings[i]:
                flag[i-1]=max(flag[i-1],flag[i]+1)
        return sum(flag)
s=Solution()
test=[
{"input":[1,0,2], "output":5},
]
for t in test:
    r=s.candy(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))