class Solution:
    def superEggDrop(self, K: int, N: int):
        if K == 0:
            return 0
        if K == 1:
            return N
        dp=[[0 for j in range(K+2)] for i in range(N+2)]
        for i in range(1,N+1):
            for j in range(1,K+1):
                dp[i][j]=dp[i-1][j]+dp[i-1][j-1]+1;
                if dp[i][j] >= N:
                    return i
        return -1

s=Solution()
test=[

{"input":[1,2], "output":2},
{"input":[2,6], "output":3},
]

for t in test:
    r=s.superEggDrop(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
