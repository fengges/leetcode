class Solution:
    def possibleBipartition(self, N, dislikes):
        tmp=[False for i in range(N+1)]
        dic={k:[] for k in range(1,N+1)}
        for dislike in dislikes:
            dic[dislike[0]].append(dislike[1])
            dic[dislike[1]].append(dislike[0])
        group1=[]
        group2=[]
        for t in range(1,len(tmp)):
            if tmp[t]==False:
                if self.find(group1,dic[t]):
                    for a in dic[t]:
                        if self.find(group2,dic[a]):
                            pass
    def find(self,A,B):
        for b in B:
            try:
                A.index(b)
                return False
            except:
                pass
        return True