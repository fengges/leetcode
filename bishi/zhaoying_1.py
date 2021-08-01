import  sys
import collections

line=sys.stdin.readline().strip()
l=line.split(',')

dict=collections.Counter(l)
t=max(dict.items(),key=lambda x:x[1])
if t[1]>len(l)/2:
    print(t[0])
else:
    print("NULL")

