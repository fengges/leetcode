import math
class Solution:
    def arrangeCoins(self, n):
        return int((math.sqrt(n*8+1)-1)/2)
