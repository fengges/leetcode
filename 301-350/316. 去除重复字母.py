class Solution:
    def removeDuplicateLetters(self, s):
        dic={}
        t=""
        for i in s:
            if i not in dic:
                t+=i
                dic[i]=0
        return t