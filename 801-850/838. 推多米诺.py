class Solution:
    def pushDominoes(self, dominoes):
        LR=[ [c,i] for i,c in enumerate(dominoes) if c!="."]
        if len(LR)==0:
            return dominoes
        start=-1
        r=["." for c in dominoes]
        for i,c in enumerate(dominoes):
            if c==".":
                if start==-1 :
                    if LR[0][0]=="L":
                        r[i]="L"
                elif start==len(LR)-1:
                    if LR[-1][0]=="R":
                        r[i]="R"
                elif LR[start][0]=="L" and LR[start+1][0]=="R":
                    continue
                elif LR[start][0]=="R" and LR[start+1][0]=="L":
                    if i-LR[start][1]>LR[start+1][1]-i:
                        r[i] = "L"
                    elif i-LR[start][1]<LR[start+1][1]-i:
                        r[i]="R"
                else:
                    r[i]=LR[start][0]
            else:
                start+=1
                r[i]=c
        return "".join(r)

s=Solution()
test=[
{"input": ".L.R...LR..L..", "output":"LL.RR.LLRRLL.."},
{"input": "RR.L", "output":"RR.L"},
]

for t in test:
    r=s.pushDominoes(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))