class Solution:
    def sortSentence(self, s: str) -> str:
        arr=[[a[:-1],a[-1]] for a in s.split(' ')]
        arr.sort(key=lambda x:x[1])
        return ' '.join([a[0] for a in arr])