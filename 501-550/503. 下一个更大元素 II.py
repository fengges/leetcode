class Solution:
    def nextGreaterElements(self, nums):
        res=[-1 for n in nums]
        s=[]
        size=len(nums)
        for i in range(size*2):
            j=i%size
            while len(s)!=0 and nums[s[-1]]<nums[j]:
                res[s[-1]]=nums[j]
                s.pop()
            s.append(j)
        return res