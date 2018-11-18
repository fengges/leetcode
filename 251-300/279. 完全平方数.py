import math
class Solution:
    def numSquares(self, n):
        dp=[i for i in range(n+1)]
        flag=[True for i in range(n+1)]
        flag[0]=False
        que=[]
        for i in range(1,int(math.sqrt(n))+1):
            quart=i*i
            dp[quart]=1
            que.append(quart)
            flag[quart]=False
            if quart==n:
                break
        while len(que)>0:
            tmp=que[0]
            que.pop(0)
            for i in range(int(math.sqrt(n-tmp)+1)):
                quart=i*i+tmp
                if flag[quart]:
                    dp[quart]=dp[tmp]+1
                    flag[quart]=False
                    que.append(quart)
            if not flag[n]:
                break
        return dp[n]
s=Solution()
test=[
{"input":12, "output":3},
{"input":8285, "output":2},
{"input":6730, "output":2},
{"input":293, "output":2},
{"input":13, "output":2},

]
for t in test:
    r=s.numSquares(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
