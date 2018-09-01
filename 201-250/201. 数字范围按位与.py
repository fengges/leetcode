class Solution:
    def rangeBitwiseAnd(self, m, n):
        count = 0
        while n != m:
            m >>= 1
            n >>= 1
            count+=1
        return m << count


s=Solution()

test=[
{"input":[600000000,2147483647],"output":4},
{"input":[5,7],"output":4},
{"input":[0,1],"output":0},

]


for t in test:
    r=s.rangeBitwiseAnd(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))