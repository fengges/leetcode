import sys

line = sys.stdin.readline().strip()
values=list(map(int, line.split()))

t,k=values[0],values[1]
tmp=[]
for i in range(t):
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    tmp.append(values)

maxn=max(tmp,key=lambda x:x[1])[1]
size=len(maxn)//k

dp=[[0 for i in range(size+1)] for j in range(maxn+1)]

for i in range(maxn+1):
    dp[i][0]=1

for i in range(1,maxn+1):
    if i-k>=0:
        for j in range(size-1):
            dp[i][j+1]+=dp[i-k]


