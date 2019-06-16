import copy
class Solution:
    def findUnsortedSubarray(self, nums):
        tmp=copy.deepcopy(nums)
        tmp.sort()
        start,end=0,len(tmp)-1
        while start<len(tmp)and nums[start]==tmp[start]:
            start+=1
        while end>=0 and nums[end]==tmp[end]:
            end-=1
        return end-start+1 if end>=start else 0