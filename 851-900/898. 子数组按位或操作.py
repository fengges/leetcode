class Solution:
    def subarrayBitwiseORs(self, A):
        res, cur, cur2=set(),set(),set()
        for i in  A:
            cur2 = {i}
            for j in cur:
                cur2.add(i | j)
            cur = cur2
            for j in  cur:
                res.add(j)
        return len(res)
s=Solution()

test=[
{"input":[1,1,2],"output": 3},
]
for t in test:
    r=s.subarrayBitwiseORs(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))



