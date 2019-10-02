import sys
N=int(sys.stdin.readline().strip())
def func(st):
    size=len(st)
    if size>=11:
        index=st.find("8")
        if index==-1:
            return False
        return len(st)-index>=11
    return False
for i in range(N):
    line=sys.stdin.readline().strip()
    line=sys.stdin.readline().strip()
    ans=func(line)
    if ans:
        print("YES")
    else:
        print("NO")


