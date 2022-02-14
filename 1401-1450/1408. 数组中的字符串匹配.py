class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans=set()
        for w in words:
            for w2 in words:
                if w2!=w and w2.find(w)>=0:
                    ans.add(w)
        return list(ans)