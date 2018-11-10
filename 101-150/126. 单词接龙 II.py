class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return []
        if beginWord not in wordList:
            wordList.insert(0,beginWord)
        head=[[] for i in wordList]
        dic={v:i for i,v in enumerate(wordList)}
        alf="qwertyuiopasdfghjklzxcvbnm"
        for word in wordList:
            if word=='lend':
                print()
            for i in range(len(word)):
                tmp_s=word[0:i]
                tmp_e=word[i+1:]
                for j in alf:
                    tmp_w=tmp_s+j+tmp_e
                    if tmp_w in dic and tmp_w!=word:
                        head[dic[word]].append(dic[tmp_w])
        start = dic[beginWord]
        end=dic[endWord]
        path=[[] for i in wordList]
        path[start].append([beginWord])
        vector=[start]
        while len(vector)!=0:
            start=vector[0]
            words=head[start]
            for w in words:
                if len(path[w])==0 or len(path[start][0])+1<=len(path[w][0]):
                    tmp=[[i for i in p] for p in path[start]]
                    for t in tmp:
                        t.append(wordList[w])
                        path[w].append(t)
                    if w not in vector:
                        vector.append(w)
            del vector[0]
        return path[end]
s=Solution()
test=[

{"input": ["hit","cog",["hot","dot","dog","lot","log"]], "output":[]},
]

for t in test:
    r=s.findLadders(t['input'][0],t['input'][1],t['input'][2])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))