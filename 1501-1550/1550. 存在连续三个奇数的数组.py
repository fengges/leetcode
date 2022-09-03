class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        r=0
        l=0
        for a in arr:
            if a%2==1:
                l+=1
                r=max(r,l)
            else:
                l=0
        return r>=3