class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:]+s[0:n]