class Solution:
    def convert(self, s, numRows):
        size=2*numRows-2
        if size==0:
            size=1
        lens=len(s)
        ss=0
        dic=[]
        while ss<lens:
            t=[a for a in s[ss:ss+size]]
            for i in range(1,numRows-1):
                if i<len(t) and (size-i)<len(t):
                    t[i]+=t[size-i]
            dic.append(t)
            ss+=size
        r=''
        for i in range(numRows):
            for d in dic:
                if i<len(d):
                    r+=d[i]
        return r

s=Solution()
test=[
{"input":["A",1],"output":"A"},
{"input":["PAYPALISHIRING",3],"output":"PAHNAPLSIIGYIR"},
{"input":["PAYPALISHIRING",4],"output":"PINALSIGYAHRPI"},
      ]

for t in test:
    r=s.convert(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.convert(t['input'][0], t['input'][1])