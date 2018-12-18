class Solution:
    def isSelfCrossing(self, x):
        n = len(x)
        for i in range(n):
            if (i + 3 < n and x[i] >= x[i + 2] and x[i + 1] <= x[i + 3]) :
                return True
            if (i + 4 < n and x[i + 1] == x[i + 3] and x[i] + x[i + 4] >= x[i + 2]) :
                return True
            if (i + 5 < n and x[i] < x[i + 2] and x[i + 4] < x[i + 2] and x[i + 2] <= x[i] + x[i + 4] and x[i + 1] < x[i + 3] and x[i + 3] <= x[i + 1] + x[i + 5]):
                return True
        return False



s=Solution()
test=[
{"input": [2,1,1,2], "output":True},
{"input": [1,2,3,4], "output":False},
{"input": [1,1,1,1], "output":True},
]

for t in test:
    r=s.isSelfCrossing(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
