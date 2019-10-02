import sys
line= sys.stdin.readline().strip()
M=int(line)
ans=0
while M:
    if M%2==1:
        ans+=1
    M=M>>1
    # print(M)
print(ans)