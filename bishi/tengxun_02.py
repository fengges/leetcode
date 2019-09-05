import sys
import functools
def cmp(a,b):
    return -(a[0]-a[1])+(b[0]-b[1])
N=int(sys.stdin.readline().strip())
values=[]
for i in range(N):
    line = sys.stdin.readline().strip()
    t= list(map(int, line.split()))
    values.append(t)
values.sort(key=functools.cmp_to_key(cmp))
ans=0
for i,v in enumerate(values):
    ans+=(v[0]*i+(N-1-i)*v[1])
print(ans)