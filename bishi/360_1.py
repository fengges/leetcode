import sys
line = sys.stdin.readline().strip()
values = list(map(int, line.split()))
N,M=values[0],values[1]
tmp=[[0]*(M+2)]
for i in range(N):
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    value = list(map(int, line.split()))
    value=[0]+value+[0]
    tmp.append(value)
tmp.append([0]*(M+2))
# tmp是矩阵 原来是 2 1
#                 1  1
# 我前后加 0   变成   0 0 0 0
#                     0 2 1 0
#                     0 1 1 0
#                     0 0 0 0
# 方便计算
r=0
for i in range(1,N+2):
    for j in range(1,M+2):
        if tmp[i][j]>0:
            r+=2
        r+=abs(tmp[i][j]-tmp[i][j-1])
        r+=abs(tmp[i][j]-tmp[i-1][j])
print(r)