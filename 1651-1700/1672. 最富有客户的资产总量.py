class Solution:
    def maximumWealth(self, accounts) -> int:
        return max([sum(a) for a in accounts])