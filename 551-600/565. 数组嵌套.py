from util.link import ListNode
class Solution(object):
    def arrayNesting(self, nums):
        dic=[]
        flag=[True for i in nums]
        flag[0]=False
        for i in range(1,len(nums)):
            if flag[i]:
                dic[nums[i]]=[nums[i]]
                while True:
                    pass