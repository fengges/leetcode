class Solution:
    def validPalindrome(self, s: str):
        if self.judge(s):
            return True
        else:
            left, right = 0, len(s) - 1
            while left<right:
                if s[left]==s[right]:
                    left+=1
                    right-=1
                else:
                    break
            if left>=right:
                return True
            else:
                return self.judge(s[:left]+s[left+1:]) or self.judge(s[:right]+s[right+1:])
    def judge(self,s):
        tmp=[i for i in s]
        tmp.reverse()
        return ''.join(tmp)==s
s=Solution()
test=[
{"input":"deeee", "output":True},
{"input":"abc", "output":False},
]

for t in test:
    r=s.validPalindrome(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))