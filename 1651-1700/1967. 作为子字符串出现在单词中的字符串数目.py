class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return len([1 for p in patterns if p.find(word)>=0])