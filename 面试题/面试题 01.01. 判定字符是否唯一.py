import collections
class Solution:
    def isUnique(self, astr: str) -> bool:
        ans=collections.Counter(astr)
        return len([a for a in ans if ans[a]>1])>0