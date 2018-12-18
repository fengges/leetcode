class Solution:
    def maxProduct(self, words):
        flag=[0 for w in words]
        for i in range(len(flag)):
            for w in words[i]:
                flag[i]|=1<<(ord(w)-ord('a'))
        r=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if flag[i]&flag[j]==0:
                    r=max(r,len(words[i])*len(words[j]))
        return r

