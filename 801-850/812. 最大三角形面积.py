
class Solution:
    def largestTriangleArea(self, points):
        s = 0
        for i in range(len(points)-2):
            for j in range(i+1,len(points)-1):
                for k in range(j+1,len(points)):
                    s = max(s,abs( 1.0 / 2 * ( points[k][0] * points[j][1] + points[j][0] * points[i][1] + points[i][0] * points[k][1] - points[j][1] *points[i][0] - points[k][1] * points[j][0] - points[k][0] * points[i][1])))
        return s


s=Solution()
test=[
{"input": [[8,3],[5,6],[3,5]],"output":4.5},
]

for t in test:
    r=s.largestTriangleArea(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))