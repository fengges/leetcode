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



s=Solution()
test=[
{"input": [4,2], "output": [
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]},
]

for t in test:
    r=s.combine(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.combine(t['input'][0], t['input'][1])