class Solution:
    def nextGreaterElements(self, nums):

        r=[]
        r.index()
        for n in range(len(nums)):
            r.append(self.find(n,nums))
        return r
    def find(self,index,nums):
        for i in range(1,len(nums)):
            if nums[(i+index)%len(nums)]>nums[index]:
                return nums[(i+index)%len(nums)]
        return -1