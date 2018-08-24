class Solution:
    def firstUniqChar(self, s):
        dic={}
        for n in s:
            if n not in dic:
                dic[n]=0
            dic[n]+=1
        for index,v in enumerate(s):
            if dic[v]==1:
                return index
        return -1