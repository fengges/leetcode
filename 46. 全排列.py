import copy
class Solution:
    def permute(self, nums):
        t=[]
        self.result = []
        index=[False for i in range(len(nums))]
        self.isSelect(index,nums,t)
        return self.result
    def isSelect(self,index,nums,t):
        if self.count(index)==len(nums):
            self.result.append(copy.deepcopy(t))
            return
        for i in  range(len(index)):
            if not index[i]:
                index[i]=True
                t.append(nums[i])
                self.isSelect(index,nums,t)
                del t[-1]
                index[i]=False

    def count(self,index):
        num=0
        for i in index:
            if i:
                num+=1
        return num

s=Solution()

test=[
{"input":[1],"output":[
    [1]
]},
{"input":[1,2,3],"output":[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]},

      ]

for t in test:
    r=s.permute(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.permute(t['input'])


