class Solution:
    def minDeletionSize(self, A):
        return sum(list(a) != sorted(a) for a in zip(*A))
