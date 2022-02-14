import collections
class Solution:
    def groupAnagrams(self, strs) :
        dicts={}
        for s in strs:
            dic=collections.Counter(s)
            tmp=sorted(dic.items(),key=lambda x:x[0])
            keys=''.join([t[0]+str(t[1]) for t in tmp])
            if keys not in dicts:
                dicts[keys]=[]
            dicts[keys].append(s)
        return [dicts[k] for k in dicts]