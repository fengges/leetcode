import copy
class Solution:
    def combine(self, n,k):
        t=[]
        self.result = []
        nums=[ i+1 for i in  range(n)]
        index=[False for i in range(len(nums))]
        self.isSelect(index,nums,t,k,0)
        return self.result
    def isSelect(self,index,nums,t,k,s):
        if k==0:
            self.result.append(copy.deepcopy(t))
            return
        for i in  range(s,len(index)):
            if not index[i]:
                index[i]=True
                t.append(nums[i])
                self.isSelect(index,nums,t,k-1,i+1)
                del t[-1]
                index[i]=False