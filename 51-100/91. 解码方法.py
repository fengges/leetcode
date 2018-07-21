class Solution:
    def numDecodings(self, s):
        if len(s)==0 or s[0]=="0":
            return 0
        result=[1]
        for i,t in enumerate([a for a in s]):
            if i!=0 and int(s[i-1:i+1])==0:
                return 0
            elif i!=0 and int(s[i-1:i+1])<=26 and t!="0" and s[i-1]!="0" :
                if i+1<len(s) and s[i+1]=="0":
                    result.append(result[-1])
                else:
                    result.append(result[-1]+1)
            elif t=="0" and i==len(s)-1 and int(s[i-1:i+1])>26:
                result.append(0)
            else:
                result.append(result[-1] )
        return result[-1]

s=Solution()
test=[
{"input":"230", "output": 0},
{"input":"110", "output": 1},
{"input":"100", "output": 0},
{"input":"101", "output": 1},

{"input":"10", "output": 1},
{"input":"12", "output": 2},
{"input":"226", "output": 3},
]

for t in test:
    r=s.numDecodings(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.numDecodings(t['input'])
