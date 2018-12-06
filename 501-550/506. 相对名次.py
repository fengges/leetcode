class Solution:
    def findRelativeRanks(self, nums):
        dic={}
        for i,v in enumerate(nums):
            dic[v]=i
        nums.sort(reverse=True)
        r=['' for i in nums]
        for i,k in enumerate(nums):
            r[dic[k]]=self.getName(i)
        return r
    def getName(self,i):
        if i==0:
            return "Gold Medal"
        elif i==1:
            return "Silver Medal"
        elif i==2:
            return "Bronze Medal"
        else:
            return str(i+1)
