import random
class RandomizedCollection:
    def __init__(self):
        self.dic=[]

    def insert(self, val):
        if val in self.dic:
            self.dic.append(val)
            return False
        else:
            self.dic.append(val)
            return True

    def remove(self, val):
        if val in self.dic:
            del self.dic[self.dic.index(val)]
            return True
        else:
            return False


    def getRandom(self):
        index=random.randint(0,len(self.dic)-1)
        return self.dic[index]