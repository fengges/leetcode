class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
class Solution:
    def maxPoints(self, points):
        res = 0
        if len(points)==0:
            return res
        for i in range(len(points)):
            dic = {}
            copy=1
            for j in range(i+1,len(points)):
                dx = points[j].x - points[i].x
                dy = points[j].y - points[i].y
                if dx==0 and dy==0:
                    copy+=1
                    continue
                d = self.gcd(dx, dy)
                a,b=dx / d, dy / d
                if a not in dic:
                    dic[a]={}
                if b not in dic[a]:
                    dic[a][b]=0
                dic[a][b]+=1
            res = max(copy, res)
            for a in dic:
                for b in dic[a]:
                    res=max(dic[a][b]+copy,res)
        return res
    def gcd(self,a,b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)
def list2point(list):
    return [Point(p[0],p[1]) for p in list]
s=Solution()
test=[
{"input":list2point([[0,0],[0,0]]), "output":2},
{"input":list2point([[1,1],[2,2],[3,3]]), "output":3},
{"input":list2point([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]), "output":4},
]
for t in test:
    r=s.maxPoints(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
