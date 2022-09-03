class Solution:
    def repair(self,ranges,postions):
        dicts={}
        flag=[True for i in ranges]
        for p in postions:
            dicts[p]=[]
            for i,r in enumerate(ranges):
                if p>=r[0] and p<=r[1]:
                    dicts[p].append(i)
        self.ans=0
        size=len(postions)
        def dps(index,result):
            if index>=size:
                return
            pep=dicts[postions[index]]
            for r in pep:
                if flag[r]:
                    flag[r]=False
                    self.ans=max(self.ans,result+1)
                    dps(index+1,result+1)
                    flag[r]=True
            dps(index+1,result)
        dps(0,0)
        return self.ans
s=Solution()

test=[
    {"input":[[[1,1],[3,6],[9,12]],[3,2,6,5]],"output":5},

    {"input":[[[1,2],[5,5],[4,11],[5,6],[1,3],[5,6]],[6,4,5,2,3,1,10]],"output":5},

]
for t in test:
    r=s.repair(*t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))