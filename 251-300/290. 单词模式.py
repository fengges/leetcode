class Solution:
    def wordPattern(self, pattern, str):
        words=str.split(" ")
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

s=Solution()
test=[
    {"input": ["ab", "dog dog"], "output": False},
    {"input": ["abba", "dog cat cat fish"], "output": False},
{"input": ["abba","dog dog dog dog"], "output":False},


{"input": ["abba","dog cat cat dog"], "output":True},
]

for t in test:
    r=s.wordPattern(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.wordPattern(t['input'][0], t['input'][1])