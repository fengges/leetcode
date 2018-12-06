
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
    def findByChar(self,char):
        tmp=self.child[self.count(char)]
        return tmp
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
class Solution:
    def findWords(self, board, words):
        tree=Trie()
        r=[]
        mark = [[True for t in temp] for temp in board]
        for w in words:
            tree.insert(w)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.search(board,mark,i,j,tree.node,r,'')
        return list(set(r))
    def search(self, borad, mark, i, j,node,r,pa):

        if i < 0 or i >= len(borad) or j < 0 or j >= len(borad[0]) or not mark[i][j]:
            return
        path=pa+borad[i][j]
        mark[i][j] = False
        tmp=node.findByChar(borad[i][j])
        if tmp:
            if tmp.flag:
                r.append(path)
            self.search(borad, mark, i + 1, j,tmp,r,path)
            self.search(borad, mark, i - 1, j,tmp,r,path)
            self.search(borad, mark, i, j + 1,tmp,r,path)
            self.search(borad, mark, i, j - 1,tmp,r,path)
        mark[i][j] = True

s=Solution()
test=[
{"input":[[["b","a","a","b","a","b"],["a","b","a","a","a","a"],["a","b","a","a","a","b"],["a","b","a","b","b","a"],["a","a","b","b","a","b"],["a","a","b","b","b","a"],["a","a","b","a","a","b"]],["aab","bbaabaabaaaaabaababaaaaababb","aabbaaabaaabaabaaaaaabbaaaba","babaababbbbbbbaabaababaabaaa","bbbaaabaabbaaababababbbbbaaa","babbabbbbaabbabaaaaaabbbaaab","bbbababbbbbbbababbabbbbbabaa","babababbababaabbbbabbbbabbba","abbbbbbaabaaabaaababaabbabba","aabaabababbbbbbababbbababbaa","aabbbbabbaababaaaabababbaaba","ababaababaaabbabbaabbaabbaba","abaabbbaaaaababbbaaaaabbbaab","aabbabaabaabbabababaaabbbaab","baaabaaaabbabaaabaabababaaaa","aaabbabaaaababbabbaabbaabbaa","aaabaaaaabaabbabaabbbbaabaaa","abbaabbaaaabbaababababbaabbb","baabaababbbbaaaabaaabbababbb","aabaababbaababbaaabaabababab","abbaaabbaabaabaabbbbaabbbbbb","aaababaabbaaabbbaaabbabbabab","bbababbbabbbbabbbbabbbbbabaa","abbbaabbbaaababbbababbababba","bbbbbbbabbbababbabaabababaab","aaaababaabbbbabaaaaabaaaaabb","bbaaabbbbabbaaabbaabbabbaaba","aabaabbbbaabaabbabaabababaaa","abbababbbaababaabbababababbb","aabbbabbaaaababbbbabbababbbb","babbbaabababbbbbbbbbaabbabaa"]], "output":[]},
{"input":[[["a","a"]],["aaa"]], "output":[]},

{"input":[[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],["oath","pea","eat","rain"]], "output":["eat","oath"]},

]
for t in test:
    r=s.findWords(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
