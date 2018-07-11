class Solution:
    def longestPalindrome(self, s):
        if len(s)==1:
            return s
        elif len(s)==2 and s[0]==s[1]:
            return s
        maxL=0
        maxS=len(s)
        maxE=0
        n=len(s)*2-3
        for i in range(n+1):
            if i%2==0:
                st=i/2-1
                e=i/2+1
                l = 1
            else:
                st=i/2-0.5
                e=i/2+0.5
                l=0
            st=int(st)
            e=int(e)

            while st>=0 and e<len(s) and s[st]==s[e]:
                st-=1
                e+=1
                l+=2
            if l>maxL:
                maxL=l
                maxS=st+1
                maxE=e
        return s[maxS:maxE]

s=Solution()

test=[
{"input":"abb","output":"bb"},
{"input":"ccc","output":"ccc"},
{"input":"a","output":"a"},
    {"input":"babad","output":"bab"},
        {"input":"cbbd","output":"bb"},
      ]

for t in test:
    r=s.longestPalindrome(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.longestPalindrome(t['input'])

