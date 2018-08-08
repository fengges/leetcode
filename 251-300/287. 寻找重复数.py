class Solution:
    def findDuplicate(self, nums):
        dic={}
        for n in nums:
            if n in dic:
                dic[n]+=1
            else:
                dic[n]=1
        for k in dic:
            if dic[k]==2:
                return k