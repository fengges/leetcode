class Solution:
    def maxChunksToSorted(self, arr):
        tmp=[a for a in arr]
        tmp.sort()
        flag=[arr[i]==tmp[i] for i in range(len(arr))]
        r=0
        find=True
        for f in flag:
            if f:
                r += 1
                find=True
            elif find:
                find=False
        return r
s=Solution()
test=[
{"input":  [4,3,2,1,0], "output":1},
{"input":  [1,0,2,3,4], "output":4},
]

for t in test:
    r=s.maxChunksToSorted(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))