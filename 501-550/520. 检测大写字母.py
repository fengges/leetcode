class Solution:
    def detectCapitalUse(self, word):
        if len(word)==1:
            return True
        t = ord(word[0])
        if t >= 65 and t <= 90:
            i=self.isDa(word[1:])
            if i==0:
                return False
            else:
                return True
        else:
            i = self.isDa(word[1:])
            if i==-1:
                return True
            else:
                return False
    def isDa(self,s):
        n=0
        for i in s:
            t = ord(i)
            if t >= 65 and t <= 90:
                n+=1
        if n==len(s):
            return 1
        elif n==0:
            return -1
        else:
            return 0
s = Solution()
test = [
    {"input": "USA", "output":True},
]

for t in test:
    r = s.detectCapitalUse(t['input'])
    if r != t['output']:
        print("error:" + str(t) + " out:" + str(r))
        r = s.detectCapitalUse(t['input'])
