class Solution:
    def myPow(self, x, n):
        zheng=True
        if x<0:
            if n%2!=0:
                zheng=False
        if x==0 or x==1 or (x==-1 and n%2!=0):
            return x
        if x==-1 :
            return 1
        s=1
        if n>=0:
            for i in range(n):
                s*=x
                if s==0:
                    return 0
        else:
            for i in range(-n):
                s/=x
                if s==0:
                    return 0

        if not zheng:
            if -s>2147483648:
                return 0
            else:
                return s
        else:
            if s>2147483647:
                return 0
            else:
                return s

s=Solution()
test=[
{"input": [-2.00000,2], "output": 4.0000},
{"input": [2.00000,-2], "output": 0.25000},
{"input": [2.00000,10], "output": 1024.00000},
{"input": [ 2.10000,3], "output": 9.26100},


]

for t in test:
    r=s.myPow(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.myPow(t['input'][0], t['input'][1])
