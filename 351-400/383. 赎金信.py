class Solution:
    def canConstruct(self, ransomNote, magazine):
        dicA={}
        dicB={}
        for i in ransomNote:
            if i in dicA:
                dicA[i]+=1
            else:
                dicA[i]=1
        for i in magazine:
            if i in dicB:
                dicB[i]+=1
            else:
                dicB[i]=1
        for k in dicA:
            if k in dicB and dicB[k]>=dicA[k]:
                continue
            else:
                return False
        return True