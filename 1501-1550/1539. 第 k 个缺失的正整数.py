class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for a in arr:
            if a<=k:
                k+=1
            else:
                break
        return k