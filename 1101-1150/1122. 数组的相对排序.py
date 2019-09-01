import functools

class Solution:
    def relativeSortArray(self, arr1, arr2):
        size=len(arr1)
        def cmp(a, b):
            a1=arr2.index(a) if a in arr2 else size
            b1=arr2.index(b) if b in arr2 else size
            if a1==b1:
                return a-b
            return a1-b1

        tmp = sorted(arr1, key=functools.cmp_to_key(cmp))
        return tmp

s=Solution()
test=[
{"input":[[28,6,22,8,44,17],[22,28,8,6]], "output":[22,28,8,6,17,44]},
]

for t in test:
    r=s.relativeSortArray(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))