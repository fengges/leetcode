import copy
class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        self.result=[]
        self.dic={}
        self.find(nums,[],0)
        return self.result
    def find(self,nums,temp,n):
        if n==len(nums):
            s=str(temp)
            if s not in self.dic:
                self.dic[s]=0
                self.result.append(temp)
            return
        self.find(nums,temp,n+1)
        t=copy.deepcopy(temp)
        t.append(nums[n])
        self.find(nums,t,n+1)
