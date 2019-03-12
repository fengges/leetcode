class Solution:
    def lenLongestFibSubseq(self, A):
        result=[]
        for i in A:
            for r in result:
                if r[-1]<2 or r[0]+r[1]==i:
                    r[0],r[1],r[2]=r[1],i,r[2]+1
            result.append([-1,i,1])
        return max([r[-1] for r in result])
s=Solution()
test=[
{"input":[2,4,7,8,9,10,14,15,18,23,32,50], "output":5},
]

for t in test:
    r=s.lenLongestFibSubseq(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))