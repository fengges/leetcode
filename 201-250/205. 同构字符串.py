class Solution:
    def isIsomorphic(self, s, t):
        words=s
        pattern=t
        if len(words)!=len(pattern):
            return False
        dic={}
        w_dic={}
        for index,s in enumerate(pattern):
            if s in dic and dic[s]!=words[index]:
                return False
            else:
                if words[index] in w_dic and w_dic[words[index]]!=s:
                    return False
                else:
                    dic[s]=words[index]
                    w_dic[words[index]]=s
        return True