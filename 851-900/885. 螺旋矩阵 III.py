class Solution:
    def spiralMatrixIII(self, R, C, r0, c0):
        size=R*C
        h=0
        r=[[r0, c0]]
        while len(r)<size:
            h+=1
            for i in range(1,h+1):
                if (self.inSide(R, C,r0,c0+i)):
                    r.append([r0,c0+i])
            c0+=h
            for i in range(1,h+1):
                if (self.inSide(R, C, r0+i, c0 )):
                    r.append([r0+i, c0 ])
            r0+=h
            h+=1
            for i in range(1,h+1):
                if (self.inSide(R, C,r0,c0-i)):
                    r.append([r0,c0-i])
            c0-=h
            for i in range(1,h+1):
                if (self.inSide(R, C,r0-i,c0)):
                    r.append([r0-i,c0])
            r0-=h
        return r
    def inSide(self,r, c,x,y):
        return x>=0 and x<r and y>=0 and y<c
s=Solution()

test=[
{"input":[5,6,1,4],"output":[[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]},
{"input":[1,4,0,0],"output":[[0,0],[0,1],[0,2],[0,3]]},


]
for t in test:
    r=s.spiralMatrixIII(t['input'][0],t['input'][1],t['input'][2],t['input'][3])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))