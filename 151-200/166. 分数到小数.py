class Solution:
    def fractionToDecimal(self, numerator, denominator):
        if numerator==0:
            return "0"
        flag=False
        if (numerator> 0 and  denominator>0 ) or  (numerator< 0 and  denominator<0 ):
            flag=True
        numerator=abs(numerator)
        denominator=abs(denominator)
        tmp = int(numerator / denominator)
        r = str(tmp)
        numerator = numerator % denominator
        dic={numerator:0}
        if numerator!=0:
            numerator*=10
            r+='.'
        while numerator!=0:
            tmp=int(numerator/denominator)
            numerator=numerator%denominator
            r += str(tmp)
            if numerator in dic:
                index=r.find('.')+dic[numerator]+1
                r=r[0:index]+"("+r[index:]+")"
                break
            else:
                dic[numerator]=len(dic)
                numerator*=10
        if flag:
            return r
        else:
            return "-"+r
s=Solution()

test=[
{"input":[-50,8],"output":"-6.25"},
{"input":[12,99],"output":"0.(12)"},
{"input":[1,6],"output":"0.1(6)"},


{"input":[2,3],"output":"0.(6)"},
{"input":[1,2],"output":"0.5"},
{"input":[2,1],"output":"2"},

]
for t in test:
    r=s.fractionToDecimal(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
