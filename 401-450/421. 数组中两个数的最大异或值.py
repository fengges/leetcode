class Solution:
    def findMaximumXOR(self, nums):
        res,mask = 0,0
        for i in range(31,-1,-1):
            mask |= (1 << i)
            s=set()
            for num in nums:
                s.add(num & mask)
            t = res | (1 << i)
            for prefix in s:
                if t ^ prefix in s:
                    res = t
                    break
        return res
