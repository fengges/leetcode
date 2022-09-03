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
    def search2(self, word):
        return self.find2(self.node.child,word)

    def find2(self,nodes,word):
        if len(word)==0:
            return False
        tmp=nodes[self.count(word[0])]
        if tmp is None:
            return False
        if tmp.flag:
            return True
        else:
            return self.find2(tmp.child,word[1:])
    def startsWith(self, prefix):
        return self.find(self.node.child,prefix)!=None
class StreamChecker:

    def __init__(self, words):
        self.t=Trie()
        for w in words:
            self.t.insert(w[::-1])
        self.q=[]
    def query(self, letter: str) -> bool:
        self.q.append(letter)
        return self.t.search2(''.join(self.q[::-1]))

class StreamChecker2:
    def __init__(self, words):
        self.trie = {}
        self.ends = set()
        self.q = []
        for word in words:
            self.add(word)

    def add(self, word):
        node = self.trie
        for c in word[::-1]:
            if c not in node:
                node[c] = {}
            node = node[c]
        self.ends.add(id(node))

    def lookup(self):
        node = self.trie
        for i in range(len(self.q) - 1, -1, -1):
            c = self.q[i]
            if c not in node:
                return False
            node = node[c]
            if id(node) in self.ends:
                return True
        return False

    def query(self, letter: str) -> bool:
        self.q.append(letter)
        return self.lookup()

null=None
false=False
true=True
test=[
    {
        "input": {
            'function':
                ["StreamChecker","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query"],
            'parm':  [[["ab","ba","aaab","abab","baa"]],["a"],["a"],["a"],["a"],["a"],["b"],["a"],["b"],["a"],["b"],["b"],["b"],["a"],["b"],["a"],["b"],["b"],["b"],["b"],["a"],["b"],["a"],["b"],["a"],["a"],["a"],["b"],["a"],["a"],["a"]]
        },
        "output":
            [null,false,false,false,false,false,true,true,true,true,true,false,false,true,true,true,true,false,false,false,true,true,true,true,true,true,false,true,true,true,false]
    },
    {
        "input": {
            'function':
                ["StreamChecker","query","query","query","query","query","query","query","query","query","query","query","query"],
            'parm': [[["cd","f","kl"]],["a"],["b"],["c"],["d"],["e"],["f"],["g"],["h"],["i"],["j"],["k"],["l"]]
        },
        "output":
            [null,false,false,false,true,false,true,false,false,false,false,false,true]
    },

]
def getCode(function,param,name):
    return function+"("+",".join([name+"["+str(i)+"]" for i in range(len(param))]) +")"
for t in test:
    function=t['input']['function']
    parm=t['input']['parm']
    output = t['output']
    obj=eval(getCode(function[0],parm[0],"parm[0]"))
    for i in range(1,len(function)):
        r=eval("obj."+getCode(function[i], parm[i],'parm[i]'))
        if r!=output[i]:
            print("error")
            r = eval("obj." + getCode(function[i], parm[i], 'parm[i]'))
