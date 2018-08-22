class Solution:
    def isPowerOfFour(self, num):
        if num==0:
            return False
        while num!=1:
            if num%2==0:
                num=num>>2
            else:
                return False

        return True