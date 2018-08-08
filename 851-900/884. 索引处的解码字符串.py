class Solution:
    def decodeAtIndex(self, S, K):
        t=""
        for i in S:
            if i>="0" and i<"9":
                t=t*int(i)
            else:
                t+=i
            if len(t)>K:
                break
        if K>len(t):
            return ""
        return t[K-1]
s=Solution()
test=[


{"input":["a2b3c4d5e6f7g8h9",623529], "output":"o"},
{"input":["leet2code3",10], "output":"o"},
{"input":["ha22",5], "output":"h"},
{"input":["a2345678999999999999999",1], "output":"a"},
]

for t in test:
    r=s.decodeAtIndex(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.decodeAtIndex(t['input'][0], t['input'][1])
