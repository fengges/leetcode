class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        ans=''
        for w in words:
            ans+=w
            if ans==s:
                return True
        return False