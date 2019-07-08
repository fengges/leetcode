class Solution:
    def loudAndRich(self, richer, quiet) :
        tmp=[[quiet[i],[],i] for i in range(len(quiet))]
        for r in richer:
            tmp[r[0]][1].append(r[1])
        r=[i for i in range(len(tmp))]
        index=self.find(tmp)
        for j in index:
            self.count(j,tmp,r,j)
        return r
    def count(self,i,tmp,r,nmin):
        if tmp[r[i]][0]<tmp[nmin][0]:
            nmin=r[i]
        r[i]=nmin
        for j in tmp[i][1]:
            self.count(j,tmp,r,nmin)
    def find(self,tmp):
        t=set()
        for t1 in tmp:
            t|=set(t1[1])
        return {i for i in range(len(tmp))}-t

s=Solution()
test=[
{"input": [[[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]],[3,2,5,4,6,1,7,0]], "output":[5,5,2,5,4,5,6,7]},
]

for t in test:
    r=s.loudAndRich(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
