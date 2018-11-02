import copy
class Solution:
    def wordBreak(self, s, wordDict):
        if len(s)==0:
            return True
        flag=[False for i in range(len(s)+1)]
        flag[0]=True
        dic={0:[""]}
        for i in range(len(s)):
            for j in range(i+1):
                str = s[j:i + 1]
                if flag[j] and str in wordDict:
                    flag[i+1]=True
                    tmp=dic[j]
                    if i+1 not in dic:
                        dic[i+1]=[]
                    for t in tmp:
                        t1=t+" "+str
                        dic[i+1].append(t1)
        if len(s) not in dic:
            return []
        return dic[len(s)]
s=Solution()

test=[
{"input":["catsanddog", ["cat", "cats", "and", "sand", "dog"]],"output":[
  "cats and dog",
  "cat sand dog"
]},
{"input":["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
,["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]],"output":[
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
