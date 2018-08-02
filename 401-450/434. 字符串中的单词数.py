import re
class Solution:
    def countSegments(self, s):
        if len(s)==0:
            return 0
        rr = re.compile(r'[ ]+')
        size=len(rr.findall(s))
        if s[0]==' ':
            size-=1
        if s[-1]==' ':
            size-=1
        return size+1

s=Solution()
test=[
{"input": "  ", "output":0},
{"input": "love live! mu'sic forever", "output":4},
{"input": "love live! mu'sic forever", "output":4},
{"input": "Hello, my name is John", "output":5},
]

for t in test:
    r=s.countSegments(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.countSegments(t['input'])