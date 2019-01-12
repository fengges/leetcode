class Solution:
    def findMinArrowShots(self, points):
        points.sort(key=lambda x:x[0])
        size=len(points)
        if size<2:
            return size
        r,start,end=1,points[0][0],points[0][1]
        for i in range(1,size):
            if points[i][0]>end:
                start,end=points[i][0],points[i][1]
                r+=1
            else:
                start,end=points[i][0],min(end,points[i][1])
        return r

s=Solution()

test=[
{"input":[[10,16],[2,8],[1,6],[7,12]],"output":2},
]
for t in test:
    r=s.findMinArrowShots(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))