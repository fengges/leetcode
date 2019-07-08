class Solution:
    def leastBricks(self, wall):
        size=len(wall)
        dict={}
        for wa in wall:
            num=0
            for w in wa[:-1]:
                num+=w
                dict[num]=dict.get(num,0)+1
        tmp=[dict[k] for k in dict]
        tmp.append(0)
        return size-max(tmp)
s=Solution()
test=[
{"input": [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]], "output":2},
]

for t in test:
    r=s.leastBricks(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
