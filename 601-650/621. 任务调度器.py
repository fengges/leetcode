class Solution:
    def leastInterval(self, tasks, n):
        dic={}
        step=0
        for t in tasks:
            if t in dic:
                dic[t]+=1
            else:
                dic[t]=1
        
        return step

s=Solution()
test=[

{"input": [["A","A","A","B","B","B"],2], "output":8},
]

for t in test:
    r=s.leastInterval(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.leastInterval(t['input'][0], t['input'][1])
