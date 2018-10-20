class Solution(object):
    def reverseVowels(self, s):
        l,r=0,len(s)-1
        tmp=[i for i in s]
        size=r+1
        while True:
            while l<size and not self.judge(s[l]):
                l+=1
            while r>=0 and not self.judge(s[r]):
                r-=1
            if l>=r:
                break
            tmp[l],tmp[r]=tmp[r],tmp[l]
            l+=1
            r-=1
        return ''.join(tmp)

    def judge(self,s):
        tmp={'a','e','i','o','u','A','E','I','O','U'}
        if s in tmp:
            return True
        else:
            return False
