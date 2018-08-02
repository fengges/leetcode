class Solution:
    def reverseString(self, s):
        t=""
        for i in range(len(s)):
            t+=s[len(s)-1-i]
        return t

s=Solution()
test=[
{"input": "hello", "output":"olleh"},
]

for t in test:
    r=s.reverseString(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.reverseString(t['input'])