import sys
start_name= sys.stdin.readline().strip()
M=int(sys.stdin.readline().strip())
valuas=[]
for i in range(M):
    names=sys.stdin.readline().strip().split(',')
    valuas.append(set(names))
know=set()
know.add(start_name)
size=0
while size!=len(know):
    size=len(know)
    for i in range(M):
        tmp=know&valuas[i]
        if len(tmp)>0:
            for t in valuas[i]:
                know.add(t)
print(len(know))
