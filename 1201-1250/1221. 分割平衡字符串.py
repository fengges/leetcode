class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans=0
        L=0
        for a in s:
            if a=="L":
                L+=1
            else:
                L-=1
            if L==0:
                ans+=1
        return ans