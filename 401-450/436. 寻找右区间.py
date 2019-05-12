class Solution:
    def findRightInterval(self, intervals):
        tmp=[[interval[0],index] for index,interval in enumerate(intervals)]
        tmp.sort(key=lambda x:x[0])
        num=[t[0] for t in tmp]
        r=[]
        for i in intervals:
            t=self.bs2(i[1],num)
            if t:
                r.append(tmp[t][1])
            else:
                r.append(-1)
        return r
    def bs2(self,target,times):
        L, R = 0, len(times)-1
        while L <= R:
            m = L + (R - L) //2
            if times[m] < target:
                 L = m + 1
            elif times[m] > target:
                R = m - 1
            else:
                return m
        if L==len(times):
            return None
        return L

s=Solution()
test=[
{"input":[[1,2]],"output": [-1]},

]
for t in test:
    r=s.findRightInterval(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))