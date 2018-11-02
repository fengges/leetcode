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
    def startsWith(self, prefix):
        return self.find(self.node.child,prefix)!=None

trie =Trie()

t=trie.insert("apple")
t=trie.search("apple")
t=trie.search("app")
t=trie.startsWith("app")
t=trie.insert("app")
t=trie.search("app")
print(t)
