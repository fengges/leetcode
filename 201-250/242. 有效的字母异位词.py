class Solution:
    def isAnagram(self, s, t):
        s_dic={}
        t_dic={}
        for s1 in s:
            if s1 in s_dic:
                s_dic[s1]+=1
            else:
                s_dic[s1] = 1
        for s1 in t:
            if s1 in t_dic:
                t_dic[s1]+=1
            else:
                t_dic[s1] = 1
        if len(s_dic)!=len( t_dic):
            return False
        for k in s_dic:
            if k not in t_dic or s_dic[k]!=t_dic[k]:
                return False
        return True
