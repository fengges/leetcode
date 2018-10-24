class Solution(object):
    def customSortString(self, S, T):
        dic={}
        for t in T:
            if t not in dic:
                dic[t]=0
            dic[t]+=1
        tmp=''
        for s in S:
            if s in dic:
                tmp+=s*dic[s]
                dic[s]=0
        t=[k*dic[k] for k in dic if dic[k]>0]
        tmp+=''.join(t)
        return tmp
