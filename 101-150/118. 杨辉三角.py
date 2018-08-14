class Solution:
    def generate(self, numRows):
        if numRows==0:
            return []
        reuslt=[[1]]
        for i in range(1,numRows):
            temp=[1]
            up=reuslt[-1]
            for j in range(len(up)-1):
                temp.append(up[j]+up[j+1])
            temp.append(1)
            reuslt.append(temp)
        return reuslt
s=Solution()
test=[
{"input":5, "output":[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]},
]

for t in test:
    r=s.generate(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.generate(t['input'])

