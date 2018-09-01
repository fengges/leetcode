class Solution:
    def numMatchingSubseq(self, S, words):
        r=0
        index=[0 for w in words]
        for s in S:
            for i,w in enumerate(words):
                if index[i]<len(w) and w[index[i]]==s:
                    index[i]+=1
        for i,w in enumerate(words):
            if index[i]==len(w):
                r+=1
        return r

    def isSubsequence(self, s, t,dic):
        s1,s2=0,dic.get(s[0],-1)
        if s2==-1:
            return False
        while s1<len(s) and s2<len(t):
            if s[s1]==t[s2]:
                s1+=1
                s2+=1
            else:
                s2+=1
        if s1==len(s):
            return True
        else:
            return False

