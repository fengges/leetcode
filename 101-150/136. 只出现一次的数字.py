class Solution:
    def singleNumber(self, nums):
        dic={}
        for n in nums:
            if n not in dic:
                dic[n]=0
            dic[n]+=1
        for k in dic:
            if dic[k]==1:
                return k