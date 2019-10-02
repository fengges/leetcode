import  sys
line=sys.stdin.readline().strip()
N=int(line)
tmp=[]
for i in range(N):
    line = sys.stdin.readline().strip()
    values=list(map(int, line.split()))
    tmp.append(values)

tmp.sort(key=lambda x:x[0])

ans=0
start=0
r=0
for t in tmp:
    do=min(ans,t[0]-start)

    ans+=t[1]-do
    r=max(r,ans)
    start=t[0]

print(tmp[-1][0]+ans,r)


# 3
# 1 1
# 2 1
# 3 1
# 3
# 1 3
# 2 3
# 3 3