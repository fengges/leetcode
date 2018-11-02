class Solution:
    def wordBreak(self, s, wordDict):
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

s=Solution()

test=[
{"input":["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]],"output":True},
{"input":['leetcode', ["leet", "code"]],"output":True},
{"input":["applepenapple", ["apple", "pen"]],"output":True},
{"input":["catsandog", ["cats", "dog", "sand", "and", "cat"]],"output":False},
]
for t in test:
    r=s.wordBreak(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
