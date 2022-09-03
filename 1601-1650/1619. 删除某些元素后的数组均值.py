class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)//20
        return sum(arr[n:19*n])/(18*n)