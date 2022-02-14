class Solution:
    def minTimeToType(self, word: str) -> int:
        index=0
        ans=len(word)

        for s in word:
            index2=ord(s)-ord('a')
            t=abs(index2-index)

            ans+=min(26-t,t)
            index=index2
        return ans