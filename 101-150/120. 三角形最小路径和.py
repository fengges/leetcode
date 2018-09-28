class Solution:
    def minimumTotal(self, triangle):
        triangle.reverse()
        length=[0 for i in triangle[0]]
        length.append(0)
        for i,line in enumerate(triangle):
            tmp=[]
            for j,l in enumerate(line):
                tmp.append(triangle[i][j]+min(length[j],length[j+1]))
            length=tmp
        return length[0]

s=Solution()
test=[
{"input":[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
], "output":11},
]

for t in test:
    r=s.minimumTotal(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.minimumTotal(t['input'])
