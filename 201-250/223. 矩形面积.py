
class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        total= (D-B)*(C-A) + (H-F)*(G-E)
        if H < B or F > D or G < A or C < E:
            return total
        if H > D:
            y1 = D
        else:
            y1 = H
        if B < F :
            y2 = F
        else :
            y2 = B
        y = abs(y1 - y2)
        if E < A :
            x1 = A
        else :
            x1 = E
        if C < G :
            x2 = C
        else :
            x2 = G
        x = abs(x1 - x2)
        return total - x*y

s=Solution()
test=[
{"input": [-3, 0, 3, 4, 0, -1, 9, 2], "output":45},
]

for t in test:
    r=s.computeArea(t['input'][0],t['input'][1],t['input'][2],t['input'][3],t['input'][4],t['input'][5],t['input'][6],t['input'][7])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))