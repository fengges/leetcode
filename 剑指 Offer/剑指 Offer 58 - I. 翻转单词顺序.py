class Solution:
    def reverseWords(self, s: str) -> str:
        t=s.split(' ')
        t=[a for a in t if a]
        t.reverse()
        return ' '.join(t).strip()