class Solution:
    def bagOfTokensScore(self, tokens, P):
        tokens.sort()
        l,r=0,len(tokens)-1
        ans,sorce=0,0
        while l<=r:
            if tokens[l]>P:
                if ans>0:
                    ans-=1
                    P+=tokens[r]
                    r-=1
                else:
                    break
            else:
                P-=tokens[l]
                l+=1
                ans+=1
                sorce=max(sorce,ans)
        return sorce
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
