class Solution:
    def findDuplicates(self, nums):
        dic={}
        r=[]
        for n in nums:
            if n not in dic:
                dic[n]=0
            dic[n]+=1

        for k in dic:
            if dic[k]>1:
                r.append(k)
        return r
