class Solution:
    def divide(self, dividend, divisor):
        if divisor==1:
            return dividend
        if divisor==-1:
            if dividend==-2147483648:
                return 2147483647
            else:
                return -dividend
        sign=(dividend>0)^(divisor>0)
        end=abs(dividend)
        sor=abs(divisor)
        res=0
        while end>=sor:
            r=1
            temp=sor
            while end>(temp<<1):
                temp<<=1
                r<<=1
            res+=r
            end-=temp
        if sign:
            return -res
        else:
            return res



s=Solution()

test=[
{"input": [10,3],"output":3},
{"input":[7,-3],"output":-2},
      ]

for t in test:
    r=s.divide(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.divide(t['input'][0],t['input'][1])

