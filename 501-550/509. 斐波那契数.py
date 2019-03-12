class Solution:
    def fib(self, N):
        if N<=1:
            return N
        tmp=[0,1]
        for i in range(2,N+1):
            tmp.append(tmp[i-1]+tmp[i-2])
        return tmp[-1]
s=Solution()

test=[
{"input":3,"output": 2},
]
for t in test:
    r=s.fib(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
