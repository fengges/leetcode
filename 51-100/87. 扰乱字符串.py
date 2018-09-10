class Solution:
    def isScramble(self, s1, s2):
        if len(s1)!=len(s2):
            return False
        if s1==s2:
            return True
        a=[c for c in s1]
        a.sort()
        b=[c for c in s2]
        b.sort()
        if a!=b:
            return False
        for i in range(1,len(s1)):
            if (self.isScramble(s1[0:i],s2[0:i]) and self.isScramble(s1[i:],s2[i:])) or (self.isScramble(s1[0:i],s2[len(s2)-i:]) and self.isScramble(s1[i:],s2[0:len(s2)-i])):
                return True
        return False
test = [
{"input": ["abcdefghijklmn","efghijklmncadb"], "output":True},
{"input": ["abb","bab"], "output":True},
{"input": ["abab","aabb"], "output":True},
{"input": ["abb","bba"], "output":True},
{"input": ["great","rgeat"], "output":True},
{"input": ["abcde","caebd"], "output": False},
]
s = Solution()
for t in test:
    r = s.isScramble(t['input'][0], t['input'][1])
    if r != t['output']:
        print("error:" + str(t) + " out:" + str(r))
        r = s.isScramble(t['input'][0], t['input'][1])