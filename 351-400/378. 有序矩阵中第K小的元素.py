class Solution:
    def kthSmallest(self, matrix, k):
        t=[]
        for m in matrix:
            t.extend(m)
        t.sort()
        return t[k-1]