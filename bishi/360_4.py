import sys
line = sys.stdin.readline().strip()
values = list(map(int, line.split()))
N,M=values[0],values[1]
tmp=[]
for i in range(M):
    line = sys.stdin.readline().strip()
    tmp.append(int(line))

def deep(index,N,step,tmp):
    if step>=len(tmp):
        flag[index]=False
        return
    s=tmp[step]
    if s<index:
        deep(index-s,N,step+1,tmp)
    if s+index<=N:
        deep(s + index, N, step + 1, tmp)
flag = [True for i in range(N + 1)]
for i in range(1,N+1):

    deep(i,N,0,tmp)

print(len([v for v in flag if v==False]))