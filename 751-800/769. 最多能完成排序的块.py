class Solution:
    def maxChunksToSorted(self, arr):
        r=0
        m=0
        for i in range(len(arr)):
            m=max(m,arr[i])
            if m==i:
                r+=1
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