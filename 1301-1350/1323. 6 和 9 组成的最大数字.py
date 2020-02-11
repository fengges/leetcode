class Solution:
    def maximum69Number (self, num: int) -> int:
        s=[a for a in str(num)]
        if "6" in s:
            s[s.index('6')]='9'
        return int("".join(s))
s=Solution()
null=None
test=[
{"input":9669,"output":9969},
]
for t in test:
    r=s.maximum69Number(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))