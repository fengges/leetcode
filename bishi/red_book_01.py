import sys
line = sys.stdin.readline().strip()
tmp=line.split(' ')
N=int(tmp[0])
arr=eval(tmp[1])

dp=[0 for i in range(N+1)]
dp[0]=1
for v in arr:
    for i in range( N + 1):
        if i+v<=N:
            dp[i+v]+=dp[i]

print(dp[N])
