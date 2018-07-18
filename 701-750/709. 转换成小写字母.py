class Solution(object):
    def toLowerCase(self, str):
        temp=''
        for s in str:
            t=ord(s)
            if t>=65 and t<=90:
                t+=32
                temp+=chr(t)
            else:
                temp+=s
        return temp

s=Solution()
test=[

{"input":"Hello", "output":"hello"},
]

for t in test:
    r=s.toLowerCase(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.toLowerCase(t['input'])
