import sys
line= sys.stdin.readline().strip()

dict={chr(c):[-1,-1] for c in range(ord("A"),ord("Z"))}

for i,v in enumerate(line):
    if dict[v][0]==-1:
        dict[v]=[i,i]
    else:
        dict[v][1]=i
dict=[dict[k] for k in dict if dict[k][0]!=-1]

dict.sort(key=lambda x:x[0])
path=[[-1,-1]]
for d in dict:
    if d[0]>path[-1][1]:
        path.append(d)
    else:
        if d[1]>path[-1][1]:
            path[-1][1]=d[1]

tmp=[str(p[1]-p[0]+1) for p in path]

print(" ".join(tmp[1:]))

