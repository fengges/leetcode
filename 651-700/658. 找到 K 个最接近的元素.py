import functools
def cmp(a,b):
    if a[1]==b[1]:
        return a[0]-b[0]
    else:
        return a[1]-b[1]
class Solution:
    def findClosestElements(self, arr, k, x):
        tmp=[[v,abs(v-x)] for v in arr]
        tmp=sorted(tmp,key=functools.cmp_to_key(cmp))
        r=[tmp[i][0] for i in range(k)]
        r.sort()
        return r

s=Solution()
test=[
{"input":[[1,2,3,4,5],4,3], "output":1},
{"input":"aab", "output":1},
]
for t in test:
    r=s.findClosestElements(t['input'][0],t['input'][1],t['input'][2])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))