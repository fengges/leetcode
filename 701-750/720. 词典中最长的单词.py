
class Solution:
    class Node:
        def __init__(self, val):
            self.val = val
            self.child = [None for i in range(26)]
            self.flag = False
        def insert(self, word):
            if len(word) > 0:
                tmp = self.child[self.count(word[0])]
                if tmp is None:
                    tmp = Solution.Node(word[0])
                    tmp.insert(word[1:])
                    self.child[self.count(word[0])] = tmp
                else:
                    tmp.insert(word[1:])
            else:
                self.flag = True

        def count(self, char):
            return ord(char) - ord('a')
    class Trie:
        def __init__(self):
            self.node = Solution.Node(None)
        def count(self, char):
            return ord(char) - ord('a')

        def insert(self, word):
            self.node.insert(word)

        def search(self, word):
            tmp = self.find(self.node.child, word)
            if tmp:
                return tmp.flag
            return False

        def find(self, nodes, word):
            tmp = nodes[self.count(word[0])]
            if tmp is None:
                return None
            if len(word) == 1:
                return tmp
            else:
                return self.find(tmp.child, word[1:])
        def startsWith(self, prefix):
            return self.find(self.node.child, prefix) != None
    def longestWord(self, words):
        words.sort()
        if len(words)==0:
            return ""
        stack=[""]
        tree=Solution.Trie()
        m=1
        r=[]
        for w in words:
            if len(w)==1 or tree.search(w[:-1]):
                tree.insert(w)
                if len(w)>m:
                    r=[w]
                    m=len(w)
                elif len(w)==m:
                    r.append(w)
        if len(r)==0:
            return ""
        else:
            r.sort()
            return r[0]

s=Solution()
test=[
{"input":  ["a","banana","app","appl","ap","apply","apple"],"output":10},
]

for t in test:
    r=s.longestWord(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
