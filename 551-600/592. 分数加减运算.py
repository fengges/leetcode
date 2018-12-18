class Solution:
    class fen:
        def __init__(self,strs):
            tmp=strs.split('/')
            self.a=int(tmp[0])
            self.b=int(tmp[1])
        def add(self,other):
             b=int(self.b/self.GCU(self.b,other.b)*other.b)
             a=int(b/self.b*self.a+b/other.b*other.a)
             t=self.GCU(a,b)
             self.b=int(b/t)
             self.a=int(a/t)

        def GCU(self,m, n):
            if not m:
                return n
            elif not n:
                return m
            elif m is n:
                return m

            while m % n:
                m, n = n, m % n

            return n
    def fractionAddition(self, expression):
        expression=expression.replace("-","+-")
        fens=expression.split('+')
        r=Solution.fen("0/1")
        for t in fens:
            if len(t)>0 and t.find('/')>0:
                r.add(Solution.fen(t))
        return str(r.a)+"/"+str(r.b)

s=Solution()
test=[
{"input": "-1/2+1/2", "output":"0/1"},
{"input": "-1/2+1/2+1/3", "output":"1/3"},
{"input": "1/3-1/2", "output":"-1/6"},
{"input": "5/3+1/3", "output":"2/1"},
]

for t in test:
    r=s.fractionAddition(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))



