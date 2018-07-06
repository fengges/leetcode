class Solution:
    def uniquePaths(self, m, n):
        fact=[1]
        for i in range(1,m+n-1):
            fact.append(fact[-1]*i)
        return int(fact[m+n-2]/(fact[m-1]*fact[n-1]))


s=Solution()
test=[
{"input": [7,3], "output": 28},
]

for t in test:
    r=s.uniquePaths(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.uniquePaths(t['input'][0], t['input'][1])