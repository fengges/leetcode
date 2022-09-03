class Solution:
    def checkString(self, s: str) -> bool:
        a=[i for i,v in enumerate(s) if s=='a']
        b=[i for i,v in enumerate(s) if s=='b']
        return max(a)<min(b)
