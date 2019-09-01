import sys
line = sys.stdin.readline().strip()
size=len(line)
dict={}

for i in range(size):
    # for j in range(i+1,size+1):
    #     t=line[i:j]
    #     dict[t]=dict.get(t,0)+1
        t=line[i]
        dict[t]=dict.get(t,0)+1
t=max(dict.items(),key=lambda x:x[1])
print(t[1])