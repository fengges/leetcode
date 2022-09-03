class Solution:
    def findClosest(self, words, word1: str, word2: str) -> int:
        ans=float('inf')
        a,b=float('-inf'),float('-inf')
        for i,w in enumerate(words):
            if w==word1:
                a=i
            if w==word2:
                b=i
            ans=min(ans,abs(a-b))
        return ans

s=Solution()

test=[
    {"input":[["I","am","a","student","from","a","university","in","a","city"]
              ,"a"
              ,"student"],"output":1},

]
for t in test:
    r=s.findClosest(*t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))