class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x,y=0,0
        dicts=set()

        dicts.add(x,y)
        for p in path:
            if p=='N':
                y+=1
            if p=='S':
                y-=1
            if p=='E':
                x+=1
            if p=='W':
                x-=1
            if (x,y) in dicts:
                return True
            dicts.add((x,y))
        return False