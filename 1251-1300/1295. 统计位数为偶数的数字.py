class Solution:
    def findNumbers(self, nums) :
        return len([1 for n in nums if len(str(n))%2==0])
