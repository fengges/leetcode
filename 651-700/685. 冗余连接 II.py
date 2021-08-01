from collections import Counter
class Solution:
    def findRedundantDirectedConnection(self, edges):
        index=[l[1] for l in edges]
        dict=Counter(index)
        tmp=[k for k in dict if dict[k]==2][0]
        e=[e for e in edges if e[1]==tmp]
        return e[-1]

s=Solution()

test=[
{"input":[[1,2], [1,3], [2,3]],"output":[2,3]},
{"input":[[1,2], [2,3], [3,4], [4,1], [1,5]],"output":[4,1]},
]
for t in test:
    r=s.findRedundantDirectedConnection(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))