class Solution:
    def countPoints(self, rings: str) -> int:
        size=len(rings)//2
        ans=[rings[2*i:2*i+2] for i in range(size)]
        dict=[set() for i in range(10)]
        for a in ans:
            dict[int(a[1])].add(a[0])
        return len([k for k in dict if len(k)==3])
s=Solution()
test=[
    {"input": "B0B6G0R6R0R6G9", "output":1},

]

for t in test:
    r=s.countPoints(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))