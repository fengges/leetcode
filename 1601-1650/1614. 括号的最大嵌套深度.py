class Solution:
    def maxDepth(self, s: str) -> int:
        ans=0
        leg=0
        for a in s :
            if a=='(':
                leg+=1
            elif a==")":
                leg-=1
            ans=max(ans,leg)
        return ans