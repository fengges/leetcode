class Solution:
    def findWords(self, words):
        r=[]
        for w in words:
            line=[]
            t=w.lower()
            for s in t:
                line.append(self.getLine(s))

            if sum(line)/len(line)==line[0]:
                r.append(w)
        return r

    def getLine(self,a):
        line1="qwertyuiop"
        line2="asdfghjkl"
        line3="zxcvbnm"
        if line1.find(a)>=0:
            return 1
        elif line2.find(a)>=0:
            return 2
        else:
            return 3

s=Solution()
test=[
{"input": ["Hello","Alaska","Dad","Peace"], "output":["Alaska","Dad"]},
{"input": ["qz","wq","asdddafadsfa","adfadfadfdassfawde"], "output":["wq","asdddafadsfa"]},
]

for t in test:
    r=s.findWords(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.findWords(t['input'])