class Solution:
    def findAndReplacePattern(self, words, pattern):
        r=[]
        for word in words:
            new=self.getDic(word,pattern)
            if new:
                r.append(word)
        return r

    def getDic(self,word,pattern):
        a={}
        b={}
        if len(word)!=len(pattern):
            return False
        for i,w in enumerate(word):
            if w in a:
                if a[w]!=pattern[i]:
                    return False
            else:
                a[w]=pattern[i]
            if pattern[i] in b:
                if b[pattern[i]]!=w:
                    return False
            else:
                b[pattern[i]] = w
        return True



s=Solution()
test=[
{"input": [["abc","deq","mee","aqq","dkd","ccc"],"abb"], "output":["mee","aqq"]},

]

for t in test:
    r=s.findAndReplacePattern(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))