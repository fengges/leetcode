class Solution:
    def preimageSizeFZF(self, K):
        n=5
        num=0
        while num<K:
            num+=self.count(n)
            n+=5
        if num==K:
            return 5
        else:
            return 0
    def count(self,n):
        num=0
        while n%5==0:
            n=n/5
            num+=1
        return num


s=Solution()
test=[
{"input":80502705, "output":5},
{"input": 92, "output":0},
{"input": 3, "output":5},
{"input": 0, "output":5},
{"input": 5, "output":0},
]

for t in test:
    r=s.preimageSizeFZF(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
