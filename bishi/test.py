# import sys
# line=sys.stdin.readline().strip()
# t=line.split(',')
# t[0],t[1]=t[0].rstrip('/'),t[1].strip('/')
#
# tmp='/'.join(t)
# print(tmp)

# import sys
# line=sys.stdin.readline().strip()
# t=line.split(' ')
# arr=list(map(int,t))
#
# def func(a,b):
#     b1,b2,b3,b4=a&15,a>>8&15,a>>16&15,a>>24
#     t=sum([b1,b2,b3,b4])%b
#     return t
#
# c,b=arr[0],arr[1]
# arr=arr[2:]
# import collections
# tmp=[func(a,b) for a in arr]
# tmp=[a for a in tmp if a<c]
# dict=collections.Counter(tmp)
# tmp=sorted(dict.items(),key=lambda x:x[1],reverse=True)
# print(tmp[0][1])


import sys
line1=sys.stdin.readline().strip()
line2=sys.stdin.readline().strip()
v=int(sys.stdin.readline().strip())

tmp=[abs(ord(a)-ord(line2[i])) for i,a in enumerate(line1)]

ans=0

for i in range(len(tmp)):
    all = 0
    for j in range(i,len(tmp)):
        all+=tmp[j]
        if all<=v:
            ans=max(j-i+1,ans)
        else:
            break
print(ans)






