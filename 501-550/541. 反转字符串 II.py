class Solution:
    def reverseStr(self, s, k):
        start=0
        tmp=""
        while start+k<len(s):
            for i in range(start+k-1,start-1,-1):
                tmp+=s[i]
            size=min(start+2*k,len(s)-1)
            for i in range(start+k,size):
                tmp += s[i]
            start =size
        for i in range(len(s)-1,start-1,-1):
            tmp+=s[i]
        return tmp
s=Solution()
test=[
{"input": ["abcdefg",2], "output":'bacdfeg'},
]

for t in test:
    r=s.reverseStr(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.reverseStr(t['input'][0], t['input'][1])