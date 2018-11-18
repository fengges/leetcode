class Solution:
    def wordBreak2(self, s, wordDict):
        if len(s)==0:
            return True
        flag=[False for i in range(len(s)+1)]
        flag[0]=True
        for i in range(len(s)):
            for j in range(i+1):
                str = s[j:i + 1]
                if flag[j] and str in wordDict:
                    flag[i+1]=True
                    break
        return flag[-1]
    def wordBreak(self, s, wordDict):
        r=[]
        if self.wordBreak2(s,wordDict):
            self.find(s,wordDict,0,len(s),r,[])
        return r
    def find(self,s,wordDict,start,end,r,path):
        if start==end:
            r.append(" ".join(path))
        else:
            for i in range(start+1,end+1):
                tmp=s[start:i]
                if tmp in wordDict:
                    path.append(tmp)
                    self.find(s,wordDict,i,end,r,path)
                    path.pop()

s=Solution()

test=[
{"input":["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]],"output":[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]},
{"input":["catsanddog", ["cat", "cats", "and", "sand", "dog"]],"output":[
  "cats and dog",
  "cat sand dog"
]},


{"input":["pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]],"output":[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]},
{"input":["catsandog", ["cats", "dog", "sand", "and", "cat"]],"output":[]},
]
for t in test:
    r=s.wordBreak(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
