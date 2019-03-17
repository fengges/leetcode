class Solution:
    def bagOfTokensScore(self, tokens, P):
        tokens.sort()
        all=sum(tokens)
        r,size=0,len(tokens)
        now=0
        while r<size:
            now+=tokens[r]
            r+=1
            if all-now+P<=now:
                r-=1
                break
        return r
s=Solution()

test=[
{"input":[[58,91],50],"output":0},
{"input":[[100],50],"output":0},
{"input":[[100,200],150],"output":1},
{"input":[[100,200,300,400],200],"output":2},
]


for t in test:
    r=s.bagOfTokensScore(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
