class Solution:
    def countNumbersWithUniqueDigits(self, n):
        if n==0:
            return 1
        r=10
        c=9
        for i in range(1,n):
            c*=(10-i)
            r+=c
        return r