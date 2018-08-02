class Solution:
    def reverseWords(self, s):
        words=s.split(" ")
        tmp=""
        for w in words:
            tmp+=self.reverseString(w)+" "
        return tmp[0:-1]
    def reverseString(self, s):
        t=""
        for i in range(len(s)):
            t+=s[len(s)-1-i]
        return t