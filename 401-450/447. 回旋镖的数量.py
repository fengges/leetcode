import collections
class Solution:

    def numberOfBoomerangs(self, points):
        def f(x1, y1):
            d = collections.Counter((x2 - x1) ** 2 + (y2 - y1) ** 2 for x2, y2 in points)
            return sum(t * t - t for t in d.values())
        return sum([f(x1, y1) for x1, y1 in points])
s=Solution()
test=[
{"input": [[0,0],[1,0],[-1,0],[0,1],[0,-1]], "output":20 },
]
for t in test:
    r=s.numberOfBoomerangs(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
