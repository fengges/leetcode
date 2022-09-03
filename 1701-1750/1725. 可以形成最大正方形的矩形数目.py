class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        ans=[min(a) for a in rectangles]
        a=max(ans)
        return len([b for b in ans if b==a])