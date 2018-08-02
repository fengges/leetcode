class Solution:
    def majorityElement(self, nums):
        dic={}
        for n in nums:
            if n not in dic:
                dic[n]=0
            dic[n]+=1
        max=None
        for k in dic:
            if max is None or dic[k]>dic[max]:
                max=k
        return max