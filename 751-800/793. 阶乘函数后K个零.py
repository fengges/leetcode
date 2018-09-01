class Solution:
    def preimageSizeFZF(self, K):
        if K==0:
            return 5
        n=K*4+1
        while True:
            if n==1:
                return 0
            elif n%5==0:
                n/=5
            else:
                return 5





s=Solution()
test=[
{"input": 0, "output":5},
{"input":80502705, "output":5},
{"input": 3, "output":5},

]

for t in test:
    r=s.preimageSizeFZF(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
