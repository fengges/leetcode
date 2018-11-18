import functools
def cmp(a,b):
    return len(a)-len(b)
class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        words.sort(key=functools.cmp_to_key(cmp))
        tmp=[]
        r=[]
        for w in words:
            if (self.wordBreak(w,tmp)):
                r.append(w)
            tmp.append(w)
        return r

    def wordBreak(self, s, wordDict):
        if len(s)==0:
            return False
        flag=[False for i in range(len(s)+1)]
        flag[0]=True
        for i in range(len(s)):
            for j in range(i+1):
                str = s[j:i + 1]
                if flag[j] and str in wordDict:
                    flag[i+1]=True
                    break
        return flag[-1]
s=Solution()
test=[
{"input":[''], "output":[]},
]
for t in test:
    r=s.findAllConcatenatedWordsInADict(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))