import random
class RandomizedSet:
    def __init__(self):
        self.dic=[]

    def insert(self, val):
        if val in self.dic:
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
r=RandomizedSet()
print(r.insert(1))
print(r.remove(2))
print(r.insert(2))
print(r.getRandom())