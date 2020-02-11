class Solution:
    def reverseWords(self, s: str) -> str:
        tmp=s.split()
        tmp=[t.strip() for t in tmp if len(tmp)>0]
        tmp.reverse()
        return " ".join(tmp)