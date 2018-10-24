class WordDictionary:
    def __init__(self):
        self.dic={}

    def addWord(self, word):
        if len(word)not in self.dic:
            self.dic[len(word)]=set()
        self.dic[len(word)].add(word)
    def search(self, word):
        size=len(word)
        if size in self.dic :
            if word in self.dic[size]:
                return True
        else:
            return False
        for k in self.dic[size]:
            if self.judge(k,word):
                return True
        return False
    def judge(self,a,b):
        if len(a)!=len(b):
            return False
        for i in range(len(a)):
            if b[i]!='.' and a[i]!=b[i]:
                return False
        return True