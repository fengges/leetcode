class Solution:
    def intToRoman(self, num):
        s=''
        dic={'100_9':'CM','100_4':'CD','10_9':'XC','10_4':'XL','1_9':'IX','1_4':'IV'}
        n={'1000':'M','500':'D','100':'C','50':'L','10':'X','5':'V','1':'I'}
        n1 = [1000,100,10,1]
        for t in n1:
            v=int(num/t)
            if v==9 or v==4:
                s+=dic[str(t)+'_'+str(v)]
            elif v>=5:
                s+=n[str(5*t)]
                for i in range(v-5):
                    s+=n[str(t)]
            else:
                for i in range(v):
                    s+=n[str(t)]
            num=num%t
        return s

s=Solution()

test=[
{"input":58,"output":"LVIII"},
{"input":9,"output":"IX"},
{"input":3,"output":"III"},
{"input":4,"output":"IV"},


{"input":1994,"output":"MCMXCIV"},
      ]

for t in test:
    r=s.intToRoman(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.intToRoman(t['input'])


