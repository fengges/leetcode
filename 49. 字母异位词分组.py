
class Solution:
    def groupAnagrams(self, strs):
        ins=[ list(s) for s in strs]
        indexs=[]
        for i in ins:
            i.sort()
            indexs.append(''.join(i))
        rs = {}
        for index,value in enumerate(indexs):
            if value in rs:
                rs[value].append(strs[index])
            else:
                rs[value]=[strs[index]]
        r=[]
        for k in rs:
            r.append(rs[k])
        return r


s = Solution()

test = [
    {"input": ["",""], "output": [
["",""]
]},
    {"input": ["tea","eat","tea"], "output": [
[""]
]},
    {"input": [""], "output": [
[""]
]},
    {"input": ["eat", "tea", "tan", "ate", "nat", "bat"], "output": [
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]},


]

for t in test:
    r = s.groupAnagrams(t['input'])
    if r != t['output']:
        print("error:" + str(t) + " out:" + str(r))
        r = s.groupAnagrams(t['input'])
