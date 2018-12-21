class Solution:
    def getHint(self, secret, guess):
        dicA={}
        for s in secret:
            if s not in dicA:
                dicA[s]=0
            dicA[s]+=1
        dicB={}
        for s in  guess:
            if s not in dicB:
                dicB[s]=0
            dicB[s]+=1
        B=0
        A=0
        for k in dicA:
            if k in dicB:
                B+=min(dicB[k],dicA[k])
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                A+=1
        return str(A)+"A"+str(B-A)+"B"
    

