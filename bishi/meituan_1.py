import sys
line= sys.stdin.readline().strip()

line= sys.stdin.readline().strip()
a=set(map(int,line.split(' ')))

line= sys.stdin.readline().strip()
b=set(map(int,line.split(' ')))

c=a&b

print(len(a-c),len(a-c),len(c))
