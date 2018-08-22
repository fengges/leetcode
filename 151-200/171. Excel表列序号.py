class Solution:
    def titleToNumber(self, s):
        sum=0
        for i in range(len(s)):
            t=ord(s[i])-ord("A")+1

            sum=sum*26+t
        return sum


s=Solution()
test=[
{"input":"A", "output":1},
{"input":"AB", "output":28},
{"input":"ZY", "output":701},
]

for t in test:
    r=s.titleToNumber(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.titleToNumber(t['input'])
