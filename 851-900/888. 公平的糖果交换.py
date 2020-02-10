class Solution:
    def fairCandySwap(self, A, B):
        sum1=sum(A)
        sum2=sum(B)
        B=set(B)
        left=sum1-sum2
        for a in A:
            if (a-left//2) in B:
                return [a,a-left//2]


s=Solution()
test=[

{"input":[[2], [1,3]], "output":[2,3]},
{"input":[[1,1], [2,2]], "output":[1,2]},
{"input":[[1,2], [2,3]], "output":[1,2]},
{"input":[[1,2,5], [2,4]], "output":[5,4]},
]

for t in test:
    r=s.fairCandySwap(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))