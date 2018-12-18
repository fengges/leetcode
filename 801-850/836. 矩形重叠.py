class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        A, B, C, D, E, F, G, H=rec1[0],rec1[1],rec1[2],rec1[3],rec2[0],rec2[1],rec2[2],rec2[3]
        return not(H <= B or F >= D or G <= A or C <= E)

s=Solution()
test=[
{"input": [[0,0,2,2],[1,1,3,3]], "output":True},
]

for t in test:
    r=s.isRectangleOverlap(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))