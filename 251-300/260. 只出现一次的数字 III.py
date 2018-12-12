class Solution:
    def singleNumber(self, nums):
        dic={}
        for i in nums:
            dic[i]=dic.get(i,0)+1
        return [k for k in dic if dic[k]==1]