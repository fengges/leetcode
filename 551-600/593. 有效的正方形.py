class Solution:
    def validSquare(self, p1, p2, p3, p4):
        t=[]
        t.append(self.dist(p1, p2))
        t.append(self.dist(p1, p3))
        t.append(self.dist(p1, p4))
        t.append(self.dist(p2, p3))
        t.append(self.dist(p2, p4))
        t.append(self.dist(p3, p4))
        t.sort()
        return t[0]==t[1] and t[0]==t[2] and t[0]==t[3] and t[4]==t[5] and t[3]<t[4]
    def dist(self,p1,p2):
        return (p1[0]-p2[0])*(p1[0]-p2[0])+(p1[1]-p2[1])*(p1[1]-p2[1])
