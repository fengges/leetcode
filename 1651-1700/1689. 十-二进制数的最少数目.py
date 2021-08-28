class Solution:
    def minPartitions(self, n: str) -> int:
        ans=[int(a) for a in n]
        return max(ans)