class Solution:
    def subarrayBitwiseORs(self, A):
        size=len(A)
        res=[[]]
        t = 0
        for i in range(size):
            t|=A[i]
            res[0].append(t)
        for i in range(size-1):
            tmp=[]
            for j in range(1,len(res[i])):
                tmp.append(A[j]|A[i])
            res.append(tmp)
        r=[]
        for i in res:
            r.extend(i)

        return len(set(r))

s=Solution()

test=[
{"input":[1,1,2],"output": 2},
]
for t in test:
    r=s.subarrayBitwiseORs(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))



