class Solution:
    def findMaxConsecutiveOnes(self, nums):
        maxLength=0
        length=0
        for n in nums:
            if n==1:
                length+=1
                if length>maxLength:
                    maxLength=length
            else:
                length=0
        return  maxLength