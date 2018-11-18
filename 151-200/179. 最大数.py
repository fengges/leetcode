import functools
def cmp(a, b):
    if a==b:
        return 0
    if len(a)>len(b):
        if a.find(b)==0:
            return cmp(a[len(b):],b)
        else:
            if a>b:
                return 1
            return -1
    else:
        if b.find(a)==0:
            return cmp(a,b[len(a):])
        else:
            if a>b:
                return 1
            return -1
class Solution(object):
    def largestNumber(self, nums):
        tmp=[str(i) for i in nums]
        tmp=sorted(tmp,key=functools.cmp_to_key(cmp),reverse=True)
        r=''.join(tmp).lstrip('0')
        if len(r)==0:
            return '0'
        return r
s=Solution()
test=[
{"input":[0,0], "output":"0"},
{"input":[3,30,34,5,9], "output":"9534330"},
{"input":[2,10], "output":"210"},
{"input":[1,1,1], "output":"111"},

{"input":[2,1,0], "output":"210"},

]

for t in test:
    r=s.largestNumber(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))

