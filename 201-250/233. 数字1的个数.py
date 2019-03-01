class Solution:
    def countDigitOne(self, n):
        count,high ,cur,b= 0,n, 0, 1
        while high > 0:
            cur = high % 10
            high //= 10
            count += high * b
            if cur == 1:
                count += n % b+1
            elif cur > 1:
                count += b
            b *= 10
        return count

