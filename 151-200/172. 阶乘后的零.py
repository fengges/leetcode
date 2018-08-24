class Solution:
    def trailingZeroes(self, n):
        num=0
        while n!=0:
            n=int(n/5)
            num+=n
        return num
