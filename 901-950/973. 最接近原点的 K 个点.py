class Solution:
    def kClosest(self, points, K):
        points=sorted(points,key=lambda x:x[0]*x[0]+x[1]*x[1])
        return points[:K]