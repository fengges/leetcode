import collections
class Solution:
    def groupAnagrams(self, strs) :
        dicts=[collections.Counter(s) for s in strs]

        dicts=[''.join([k+str(d[k]) for k in sorted([a for a in d.keys()])]) for d in dicts]

        dit={}
        for i in range(len(dicts)):
            if dicts[i] not in dit:
                dit[dicts[i]]=[]
            dit[dicts[i]].append(i)

        return [[strs[i] for i in dit[d]]  for d in dit]


