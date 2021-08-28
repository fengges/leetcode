import random
class RandomizedSet:

    def __init__(self):
        self.set=set()


    def insert(self, val: int) -> bool:
        ans=val in self.set
        self.set.add(val)
        return not ans


    def remove(self, val: int) -> bool:
        ans=val in self.set
        if ans:self.set.remove(val)
        return ans

    def getRandom(self) -> int:
        n=random.randint(0,len(self.set)-1)
        return [a for a in self.set][n]
