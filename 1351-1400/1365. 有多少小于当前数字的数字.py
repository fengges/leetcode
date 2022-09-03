class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = [0]*101

        for n in nums:
            dic[n] += 1

        return [sum(dic[0:n]) for n in nums]