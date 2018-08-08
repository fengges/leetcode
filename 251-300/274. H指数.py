class Solution:
    def hIndex(self, citations):
        citations.sort(reverse=True)
        r=False
        i=0
        for i in range(len(citations)):
            if citations[i]>i:
                continue
            else:
                r=True
                break
        if not r:
            return len(citations)
        return i

s=Solution()
test=[
{"input": [0], "output":0},
{"input": [1], "output":1},
{"input": [3,0,6,1,5], "output":3},
]

for t in test:
    r=s.hIndex(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.hIndex(t['input'])