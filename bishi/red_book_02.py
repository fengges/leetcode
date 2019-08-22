import sys
line = sys.stdin.readline().strip()

tmp=line.split(' ')
tmp=[t for t in tmp if len(t)>0]
tmp.reverse()
print(" ".join(tmp))