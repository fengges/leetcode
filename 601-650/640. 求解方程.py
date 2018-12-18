class Solution:
    class add:
        def __init__(self,sts):
            if len(sts)==0:
                self.x=0
                self.n=0
            elif sts=='x':
                self.x=1
                self.n=0
            elif sts=='-x':
                self.x=-1
                self.n=0
            elif sts[-1]=='x':
                self.x=int(sts[:-1])
                self.n=0
            else:
                self.x=0
                self.n=int(sts)
        def addOther(self,other,flag):
            self.n+=other.n*flag
            self.x+=other.x*flag

    def solveEquation(self, equation):
        expression=equation.replace("-","+-")
        fens=expression.split('=')
        left=fens[0].split('+')
        right=fens[1].split('+')
        r=Solution.add('')
        for i in left:
            r.addOther(Solution.add(i),1)
        for i in right:
            r.addOther(Solution.add(i), -1)
        if r.x==0 and r.n==0:
            return "Infinite solutions"
        elif r.x==0 and r.n!=0:
            return "No solution"
        else:
            return "x="+str(int(-r.n/r.x))
    def GCU(self, m, n):
        if not m:
            return n
        elif not n:
            return m
        elif m is n:
            return m

        while m % n:
            m, n = n, m % n

        return n


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