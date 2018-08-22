class Solution:
    def uncommonFromSentences(self, A, B):
        s=A+" "+B
        t=s.split(" ")
        dic={}
        for s in t:
            if s in dic:
                dic[s]+=1
            else:
                dic[s]=1
        return [k for k in dic if dic[k]==1]

