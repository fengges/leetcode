import re
class Solution:
    def isPalindrome(self, s):
        s=s.lower()
        rr = re.compile(r'[a-z0-9]+')
        words=rr.findall(s)
        s=''.join(words)
        for i in range(int(len(s)/2)):
            if s[i]==s[len(s)-1-i]:
                continue
            else:
                return False
        return True
s=Solution()
test=[
{"input":"0P", "output":True},
{"input":"A man, a plan, a canal: Panama", "output":True},
]

for t in test:
    r=s.isPalindrome(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.isPalindrome(t['input'])