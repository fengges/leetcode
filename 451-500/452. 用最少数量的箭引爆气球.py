class Solution:
    def findMinArrowShots(self, points):
        dic={}
        for p in points:
            for x in range(p[0],p[1]+1):
                if x not in dic:
                    dic[x]=[]
                dic[x].append(p)
        r=0
        while True:
            m=self.findMax(dic)
            if m is None:
                return r
            r+=1
            ps=[p for p in dic[m]]
            for p in ps:
                for x in range(p[0], p[1] + 1):
                    dic[x].remove(p)
    def findMax(self,dic):
        m=None
        for k in dic:
            if m is None or len(dic[k])>len(dic[m]):
                m=k
        if len(dic[m])==0:
            return None
        return m
s=Solution()

test=[
{"input":[[10,16],[2,8],[1,6],[7,12]],"output":2},
]
for t in test:
    r=s.findMinArrowShots(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))