class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        a1,a2=0,0
        for p in position:
            if p%2==0:a1+=1
            else:a2+=1
        return min(a1,a2)

