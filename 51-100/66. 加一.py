class Solution:
    def plusOne(self, digits):
        digits.reverse()
        digits.append(0)
        isJin=1
        for i,v in enumerate(digits):
            if v+isJin==10:
                digits[i]=0
                isJin=1
            else:
                digits[i]=digits[i]+isJin
                isJin=0

        if digits[-1]==0:
            del digits[-1]

        digits.reverse()


