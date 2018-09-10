
class Solution:
    def numTrees(self, n):
        dic=[0 for i in range(max(3,n+1))]
        dic[0]=1
        dic[1]=1
        dic[2]=2
        for i in range(3,n+1):
            for j in range(1,i+1):
                dic[i]+=dic[j-1]*dic[i-j]
        return dic[n]
s=Solution()
test=[
{"input":1,"output":1},
{"input":3,"output":5},
{"input":12,"output":208012},

]
for t in test:
    r=s.numTrees(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.numTrees(t['input'])