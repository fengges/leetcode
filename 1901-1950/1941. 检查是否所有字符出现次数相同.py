import collections
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dicts=collections.Counter([a for a in s])
        ans=set()
        for d in dicts:
            ans.add(dicts[d])
        return len(ans)==1