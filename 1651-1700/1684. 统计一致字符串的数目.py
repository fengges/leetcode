class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        t=set([a for a in allowed])
        tmp=[set([a for a in w]) for w in words]
        ans=[1 for a in tmp if len(a-t)==0]
        return len(ans)