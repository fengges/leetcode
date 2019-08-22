class Solution:
    def projectionArea(self, grid):
        rowMax=[max(g) for g in grid]
        columMax=[]
        for  i in range(len(grid[0])):
            columMax.append(max([x[i] for x in grid ]))
        all=0
        for g in grid:
            for i in g:
                if i!=0:
                    all+=1
        return sum(rowMax)+sum(columMax)+all


s=Solution()
test=[
{"input":[[2,1],[1,1]], "output":8},
{"input":[[1,0],[0,2]], "output":8},
{"input":[[1,1,1],[1,0,1],[1,1,1]], "output":14},
]

for t in test:
    r=s.projectionArea(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.projectionArea(t['input'])

