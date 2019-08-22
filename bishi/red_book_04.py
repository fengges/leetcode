import sys

line = sys.stdin.readline().strip()
values = list(map(int, line.split()))
N,T,M=values[0],values[1],values[2]
line = sys.stdin.readline().strip()
values = list(map(int, line.split()))

def func2(values,N,T,M):
    def judge(values,N,T,M,X):
        tmp=[v for v in values]
        if M>T:
            M=T
        T=T-M
        for i in range(N):
            t=tmp[i]//X
            if t>M:
                M=t
            tmp[i]-=X*t
            M-=t
            if M==0:
                break
        else:
            tmp.sort(reverse=True)
            for i in range(M):
                tmp[i%N]-=X
        t=[t for t in tmp if t>0]
        size=sum(t)
        return T-size
    def find(values,N,T,M):

        left, right =min(values),max(values)
        r=right
        while left<=right:
            mid=(left+right)//2
            t=judge(values,N,T,M,mid)
            if t>0:
                left=mid+1
                r=min(mid,r)
            elif t<0:
                right=mid-1
            else:
                return mid
        return r
    values=[v for v in values if v>0]
    values.sort(reverse=True)
    N=len(values)
    if T<N:
        print(-1)
    else:
        x=find(values,N,T,M)
        t=judge(values, N, T, M, x)
        if t>=0:
            print(x)
        else:
            print(-1)
        pass


def func(N, T, M, H):
    if M < N:
        return -1
    if T == N and M >= T:
        max_h = max(H)
        # 魔物个数与打击回合数相等，则一定可以击杀
        # 但是要魔力值和打击回合数相等，否则还可以分裂
        # 若魔物的生命值最大为1，则不需要魔法伤害
        # 否则，魔法伤害一定等于最大值
        #
        return 0 if max_h == 1 else max_h
    H.sort()

    # 普通攻击，保存魔力
    i = 0
    while H[i] == 1:
        T -= 1
        N -= 1
        i += 1

    # 剩下的需要魔力值，所以魔力值小于个数一定不能有结果
    if M < T:
        return -1

    # 将最大的值分裂
    H = H[i:]
    max_index = H.index(max(H))
    H.append(H[max_index]//2)
    H[max_index] -= H[max_index]//2

    return func(len(H), T, M, H)

func2(values,N, T, M)
# print(func(N, T, M, values))
