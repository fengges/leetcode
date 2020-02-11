from collections import Counter
class Solution:
    def balancedString(self, s: str) -> int:
        dict=Counter(s)
        avg=len(s)//4
        ans=0
        for k in "QWER":
            t=dict.get(k,0)-avg
            ans+=t if t>=0 else -t
        return ans//2
        pass