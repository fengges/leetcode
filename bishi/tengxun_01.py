import sys

line = sys.stdin.readline().strip()
values = list(map(int, line.split()))
N,M=values[0],values[1]

line = sys.stdin.readline().strip()
boxs = list(map(int, line.split()))

line = sys.stdin.readline().strip()
keys = list(map(int, line.split()))

b=[b%2 for b in boxs]
k=[k%2 for k in keys]

sizeb,sizek=len(b),len(k)
numb,numk=sum(b),sum(k)
ans=min(numb,sizek-numk)+min(numk,sizeb-numb)

print(ans)