
class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        if (C-A)*(D-B)<(G-E)*(H-F):
            A, B, C, D, E, F, G, H=  E, F, G, H,A, B, C, D
        flag1=False
        flag2=False
        if E>=A and E<=C and F>=B and F<=D:
            flag1=True
        if G>=A and G<=C and H>=B and H<=D:
            flag2=True
        if flag1 and flag2:
            return (C-A)*(D-B)+(G-E)*(H-F)-(C-A)*(D-B)
        elif flag1:
            return (C-A)*(D-B)+(G-E)*(H-F)-(C-E)*(D-F)
        elif flag2:
            return (G - A) * (H - B)
        else:
            return (C-A)*(D-B)+(G-E)*(H-F)

s=Solution()
test=[
{"input": [-3, 0, 3, 4, 0, -1, 9, 2], "output":45},
]

for t in test:
    r=s.computeArea(t['input'][0],t['input'][1],t['input'][2],t['input'][3],t['input'][4],t['input'][5],t['input'][6],t['input'][7])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))