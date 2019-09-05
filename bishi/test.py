import sys
def factorial_(n):
    result=1
    for i in range(2,n+1):
        result=result*i
    return result

def comb(n,m):
    a=1
    for i in range(m,n+1):
        a*=i
    return a//factorial_(n-m) #直接使用math里的阶乘函数计算组合数

line = sys.stdin.readline().strip()
values=list(map(int, line.split()))

t,k=values[0],values[1]
dict={}
def func(size,k):
    if size in dict:
        return dict[size]
    else:
        an=1
        t=size//k
        for i in range(1,t+1):
            left=size-i*k
            for j in range(1,min(i+1,left+2)):
                a=comb(left+1,j)
                an+=a
        dict[size]=an
        return an

for i in range(t):
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    l,r=values[0],values[1]
    ans=0
    for j in range(l,r+1):
        ans+=func(j,k)
    print(ans)

# 3 2
# 4 4
# 1 3
# 2 3
