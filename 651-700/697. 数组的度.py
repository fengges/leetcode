class Solution:
    def majorityElement(self, nums):
        dic={}
        size=int(len(nums)/3)
        for n in nums:
            if n not in dic:
                dic[n]=0
            dic[n]+=1
        max=[]
        for k in dic:
            if dic[k]>size:
                max.append(k)
        return max