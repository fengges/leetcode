class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxa=max(candies)
        ans=[True if c+extraCandies>=maxa else False for c in candies   ]
        return ans