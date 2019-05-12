class Stat:
    class Node:
        def __init__(self,val=[],num=0):
            self.val=val
            self.next=None
            self.pret=None
            self.num=num
        def update(self,num):
            self.num=num
        def add(self,w):
            self.val.append(w)
        def remove(self,w):
            if w in self.val:
                self.val.remove(w)
        def size(self):
            return len(self.val)
    def __init__(self):
        self.dict={}
        self.head=Stat.Node(num=float('inf'))
        self.head.pret=self.head
        self.head.next=self.head
    def addWord(self,word):
        node=self.dict.get(word)
        if node:
            if node.num+1==node.pret.num:
                node.pret.add(word)
                self.dict[word]=node.pret
            else:
                tmp=self.addNode(node.pret,[word],node.num+1)
                self.dict[word] = tmp
            node.remove(word)
            if node.size()==0:
                self.delNode(node)
        else:
            last=self.getMinNode()
            if last is None:
                tmp=self.addNode(self.head, [word],1)
                self.dict[word] = tmp
            elif last.num==1:
                last.add(word)
                self.dict[word] = last
            else:
                tmp=self.addNode(last, [word],1)
                self.dict[word] = tmp
    def delNode(self,node):
        node.pret.next=node.next
        node.next.pret=node.pret
        del node
    def addNode(self,node,val,num):
        tmp=Stat.Node(val,num)
        tmp.next=node.next
        tmp.next.pret=tmp
        node.next=tmp
        tmp.pret=node
        return tmp
    def delWord(self,word):
        node = self.dict.get(word)
        if node:
            if node.num-1==node.next.num:
                node.next.add(word)
                self.dict[word] = node.next
            else:
                tmp=self.addNode(node, [word], node.num - 1)
                self.dict[word]=tmp
            node.remove(word)
            if node.size()==0:
                self.delNode(node)
    def getMaxWord(self):
        if not self.isEmpty():
            return self.head.next.val
        return []
    def getMinWord(self):
        if not self.isEmpty():
            return self.head.pret.val
        return []
    def getMinNode(self):
        if not self.isEmpty():
            return self.head.pret
        return None
    def isEmpty(self):
        return self.head==self.head.next


if __name__=="__main__":
    t=Stat()
    t.addWord("abc")
    print(t.getMaxWord())
    print(t.getMinWord())
    print("-"*10)

    t.addWord("abc")
    t.addWord("abdfc")
    t.addWord("abc")
    print(t.getMaxWord())
    print(t.getMinWord())
    print("-"*10)

    t.addWord("a1223c")
    t.addWord("a1223c")
    t.delWord("abc")
    t.delWord("abc")
    print(t.getMaxWord())
    print(t.getMinWord())
    print("-"*10)
    pass