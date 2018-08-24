class Solution:
    def numberOfLines(self, widths, S):
        line=0
        num=0
        S=S.lower()
        for s in S:
            t=widths[ord(s)-ord('a')]
            if num+t>100:
                line+=1
                num=t
            else:
                num+=t
        return [line+1,num]

s=Solution()
test=[
{"input":[[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],"abcdefghijklmnopqrstuvwxyz"], "output":[3, 60]},
{"input":[[4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],"bbbcccdddaaa"], "output":[2,4]},

]

for t in test:
    r=s.numberOfLines(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.numberOfLines(t['input'][0], t['input'][1])


