class Solution:
    def minTimeToVisitAllPoints(self, points):
        ans=0
        def abs(n):
            return n if n>0 else -n
        def distance(a,b):
            t1=max(abs(a[0]-b[0]),abs(a[1]-b[1]))
            return t1

        for i in range(len(points)-1):
            ans+=distance(points[i],points[i+1])
        return ans