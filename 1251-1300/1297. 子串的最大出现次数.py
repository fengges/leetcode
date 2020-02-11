from collections import Counter
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        tmp=[]
        for i in range(len(s)-minSize+1):
            tmp.append(s[i:i+minSize])
        tmp=[t for t in tmp if len(Counter(t[::]))<=maxLetters]
        dict=Counter(tmp)
        if len(dict)==0:
            return 0
        t=max(dict.items(),key=lambda x:x[1])
        return t[1]
s=Solution()
null=None
test=[
{"input":[ "aababcaab",2,  3,  4],"output":2},
{"input":["aaaa",  1, 3,  3],"output":2},
]
for t in test:
    r=s.maxFreq(t['input'][0],t['input'][1],t['input'][2],t['input'][3])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
