class Solution:
    def romanToInt(self, s):
        ch=['M','D','C','L','X','V','I']
        dic={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        num=0
        for i in range(len(s)):
            if i+1<len(s) and ch.index(s[i])>ch.index(s[i+1]):
                num-=dic[s[i]]
            else:
                num+=dic[s[i]]
        return num

s=Solution()

test=[
{"input":"LVIII","output":58},
{"input":"IX","output":9},
{"input":"III","output":3},
{"input":"IV","output":4},


{"input":"MCMXCIV","output":1994},
      ]

for t in test:
    r=s.romanToInt(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.romanToInt(t['input'])
