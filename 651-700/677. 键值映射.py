class MapSum:
    def __init__(self):
        self.dic={}

    def insert(self, key, val):
        self.dic[key]=val

    def sum(self, prefix):
        return sum([self.dic[k] for k in self.dic if k.find(prefix)==0])
