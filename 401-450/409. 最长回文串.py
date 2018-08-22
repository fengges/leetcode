
class Solution:
    def longestPalindrome(self, s):
        dic={}
        for n in s:
            if n in dic:
                dic[n]+=1
            else:
                dic[n]=1
        has=False
        maxL=0
        for k in dic:
            l=dic[k]
            if l%2!=0:
                has=True
            maxL+=int(l/2)*2
        if has:
            maxL+=1
        return maxL

s=Solution()

test=[
{"input":"abccccdd","output": 7},
]
for t in test:
    r=s.longestPalindrome(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.longestPalindrome(t['input'])
