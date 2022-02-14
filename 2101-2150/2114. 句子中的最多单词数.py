class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max([len(a.split()) for a in sentences])