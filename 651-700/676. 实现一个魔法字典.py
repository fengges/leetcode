class MagicDictionary:
    def __init__(self):
        self.list=[]
    def buildDict(self, dict):
        self.list=dict
    def search(self, word):
        flag=False

        for l in self.list:
            if self.count(l,word)==1:
                flag=True
        return flag
    def count(self,a,b):
        r=0
        if len(a)!=len(b):
            return r
        for i in range(len(a)):
            if a[i]!=b[i]:
                r+=1
        return r