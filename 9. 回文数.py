class Solution:
    def isPalindrome(self, x):
        s=str(x)
        length=len(s)
        if length%2==0:
            index=int(length/2)
            for i in range(index):
                if s[i]!=s[length-1-i]:
                    return False
        else:
            index=int(length/2)
            for i in range(index):
                if s[i]!=s[length-1-i]:
                    return False
        return True

s=Solution()

test=[
{"input":121,"output":True},
{"input":-121,"output":False},
{"input":10,"output":False},
      ]

for t in test:
    r=s.isPalindrome(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.isPalindrome(t['input'])
