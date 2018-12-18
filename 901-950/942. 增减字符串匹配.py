class Solution:
    def diStringMatch(self, S):
        s,e=0,len(S)
        r=[None for i in range(e+1)]
        for i,t in enumerate(S):
            if t=="D":
                r[i]=e
                e-=1
            else:
                r[i]=s
                s+=1
        r[-1]=s
        return r
