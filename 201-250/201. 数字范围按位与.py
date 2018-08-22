class Solution:
    def rangeBitwiseAnd(self, m, n):
        t=m
        for i in range(m+1,n+1):
            t=t&i
        sum=0
        for i in range(32):
            if t&1==1:
                sum+=1
            t=t>>1
        return sum


s=Solution()

test=[
{"input":[5,7],"output":4},
{"input":[0,1],"output":0},

]


for t in test:
    r=s.rangeBitwiseAnd(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))