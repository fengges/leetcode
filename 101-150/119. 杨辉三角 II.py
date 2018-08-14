class Solution:
    def getRow(self, rowIndex):
        reuslt=[1]
        for i in range(1,rowIndex+1):
            temp=[1]
            up=reuslt
            for j in range(len(up)-1):
                temp.append(up[j]+up[j+1])
            temp.append(1)
            reuslt=temp
        return reuslt
s=Solution()
test=[
{"input":3, "output":[1,3,3,1]},
]

for t in test:
    r=s.getRow(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.getRow(t['input'])

