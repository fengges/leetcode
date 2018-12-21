import copy
class Solution:
    def findSubsequences(self, nums):
        if len(nums)==0:
            return []
        result=[]
        for i in nums:
            tmp=[[i]]
            for r in result:
                if r[-1]<=i:
                    t=copy.deepcopy(r)
                    t.append(i)
                    tmp.append(t)
            result.extend(tmp)
        dic=set()
        tmp=[]
        for r in result:
            if len(r)<=1:
                continue
            t=str(r)
            if t not in dic:
                dic.add(t)
                tmp.append(r)

        return tmp

s=Solution()

test=[
{"input":[4,6,7,7],"output":3},

]
for t in test:
    r=s.findSubsequences(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
