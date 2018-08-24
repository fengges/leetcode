class Solution(object):
    def findTheDifference(self, s, t):
        dicA={}
        dicB={}
        for i in s:
            if i in dicA:
                dicA[i]+=1
            else:
                dicA[i]=1
        for i in t:
            if i in dicB:
                dicB[i]+=1
            else:
                dicB[i]=1
        for k in dicB:
            if k not in dicA or dicB[k]>dicA[k]:
                return k
        return ""