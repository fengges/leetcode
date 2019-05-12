class Node:
    def __init__(self,val):
        self.val=val
        self.child=[None for i in range(26)]
        self.flag=False
    def insert(self,word):
        if len(word)>0:
            tmp=self.child[self.count(word[0])]
            if tmp is None:
                tmp=Node(word[0])
                tmp.insert(word[1:])
                self.child[self.count(word[0])]=tmp
            else:
                tmp.insert(word[1:])
        else:
            self.flag=True
    def count(self,char):
        return ord(char)-ord('a')
class Trie:
    def __init__(self):
        self.node=Node(None)
    def count(self,char):
        return ord(char)-ord('a')
    def insert(self, word):
        self.node.insert(word)

    def search(self, word):
        tmp=self.find(self.node.child,word)
        if tmp:
            return tmp.flag
        return False
    def find(self,nodes,word):
        tmp=nodes[self.count(word[0])]
        if tmp is None:
            return None
        if len(word)==1:
            return tmp
        else:
            return self.find(tmp.child,word[1:])
    def findWord(self,nodes,prefix,res):
        for n in nodes:
            if n:
                if n.flag:
                    res.append(prefix+n.val)
                self.findWord(n.child,prefix+n.val,res)

    def startsWith(self, prefix):
        return self.find(self.node.child,prefix)!=None
    def getStartWith(self, prefix):
        if len(prefix)!=0:
            last=self.find(self.node.child, prefix)
        else:
            last=self.node
        if last:
            res=[]
            self.findWord(last.child,"",res)
            for i in range(len(res)):
                res[i]=prefix+res[i]
            if last.flag:
                res.append(prefix)
            return res
        return []
class Solution:
    def palindromePairs(self, words):
        tree=Trie()
        for w in words:
            w1=w[::-1]
            tree.insert(w1)
        r=[]

        for i,w in enumerate(words):
            tmp=tree.getStartWith(w)
            for t in tmp:
                word=t[::-1]
                if self.judge(w+word):
                    index=words.index(word)
                    if index!=i:
                        r.append([i,index])
        return r

    def judge(self,word):
        return word[::-1]==word

s=Solution()
test=[
{"input": ["a",""], "output":[] },
{"input": ["abcd","dcba","lls","s","sssll"], "output":[[0,1],[1,0],[3,2],[2,4]] },

]
for t in test:
    r=s.palindromePairs(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))



