import sys
line = sys.stdin.readline().strip()
values = list(map(int, line.split()))
N,M=values[0],values[1]


line = sys.stdin.readline().strip()
value1 = list(map(int, line.split()))

line = sys.stdin.readline().strip()
value2 = list(map(int, line.split()))

# value1.sort()
# value2.sort(reverse=True)
# ans="0"*N
# for i in range(N):
#     r=[]
#     for j in range(N):
#         t=value1[j]+value2[(i+j)%N]
#         t=t%M
#         r.append(t)
#     r.sort(reverse=True)
#     r=[str(s) for s in r]
#     r=" ".join(r)
#     if r>ans:
#         ans=r
# print(ans)
ans="0"*N

def deep(value1,value2,path,mod):
    global ans
    if len(value1)==0:

        paths=[str(s) for s in path]
        r=" ".join(paths)
        if r>ans:
            ans=r
    tmp=[]
    m=0
    for i in value1:
        for j in value2:
            if (i+j)%mod>m:
                m=(i+j)%mod
                tmp=[[i,j]]
            elif (i+j)%mod==m:
                tmp.append([i,j])
    for t in tmp:
        value1.remove(t[0])
        value2.remove(t[1])
        path.append((t[1]+t[0])%mod)
        deep(value1,value2,path,mod)
        path.pop()
        value1.append(t[0])
        value2.append(t[1])
path=[]
mod=M
deep(value1,value2,path,mod)
# print(ans)


# ans="0"*N
value1.sort()
value2.sort(reverse=True)

for i in range(N):
    r=[]
    for j in range(N):
        t=value1[j]+value2[(i+j)%N]
        t=t%M
        r.append(t)
    r.sort(reverse=True)
    r=[str(s) for s in r]
    r=" ".join(r)
    if r>ans:
        ans=r
print(ans)