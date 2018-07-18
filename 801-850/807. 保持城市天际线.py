class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        rowMax=[max(g) for g in grid]
        columMax=[]
        for  i in range(len(grid[0])):
            columMax.append(max([x[i] for x in grid ]))
        sum=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                temp=min(rowMax[i],columMax[j])
                sum+=temp-grid[i][j]
        return sum

s=Solution()
test=[

{"input": [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]], "output":35},
]

for t in test:
    r=s.maxIncreaseKeepingSkyline(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.maxIncreaseKeepingSkyline(t['input'])