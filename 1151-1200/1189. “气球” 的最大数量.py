import collections
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dicts={'b':1,'a':1,'l':2,'o':2,'n':1}
        tmp=collections.Counter([s for s in text])
        ans=[ tmp.get(d,0)//dicts.get(d)    for d in dicts]
        return min(ans)