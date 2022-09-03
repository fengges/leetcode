class Solution:
    def numberOfMatches(self, n: int) -> int:
        if n==1:
            return 0

        return self.numberOfMatches(n//2+n%2)+n//2