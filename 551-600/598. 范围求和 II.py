class Solution:
    def maxCount(self, m, n, ops):
        if len(ops)==0:
            return m*n
        mini=None
        minj=None
        for o in ops:
            if mini is None or mini>o[0]:
                mini=o[0]
            if minj is None or minj>o[1]:
                minj=o[1]
        return minj*mini


