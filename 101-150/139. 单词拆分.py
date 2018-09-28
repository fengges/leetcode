class Solution:
    def wordBreak(self, s, wordDict):
        if len(s)==1:
            pass
        if len(s)==0:
            return True
        for i in range(1,len(s)+1):
            if s[0:i] in wordDict:
                if self.wordBreak(s[i:],wordDict):
                    return True
        return False

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
