
import sys
line = sys.stdin.readline().strip()
values = list(map(int, line.split()))
N,M=values[0],values[1]

line = sys.stdin.readline().strip()
values=list(map(int, line.split()))

all=sum(values)

if M>=N:
    print(N+1)
else:
    pass


