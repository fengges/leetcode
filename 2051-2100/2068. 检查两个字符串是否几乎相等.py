import collections
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        dicts1=collections.Counter([w for w in word1])
        dicts2=collections.Counter([w for w in word2])
        ans=float('-inf')
        ans=max(ans,max([abs(dicts1.get(k,0)-dicts2.get(k,0))   for k in dicts1]))
        ans=max(ans,max([abs(dicts1.get(k,0)-dicts2.get(k,0))   for k in dicts2]))
        return ans<=3
