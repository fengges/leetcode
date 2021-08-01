class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]):
        ans=[]
        for x,y,r in queries:
            n=0
            for a,b in points:
                if (a-x)*(a-x)+(b-y)*(b-y)<=r*r:
                    n+=1
            ans.append(n)
        return ans
