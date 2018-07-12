import copy
class Solution:
    def subsets(self, nums):
        self.result=[]
        self.find(nums,[],0)
        return self.result
    def find(self,nums,temp,n):
        if n==len(nums):
            self.result.append(temp)
            return
        self.find(nums,temp,n+1)
        t=copy.deepcopy(temp)
        t.append(nums[n])
        self.find(nums,t,n+1)
