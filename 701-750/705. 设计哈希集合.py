class MyHashSet:
    def __init__(self):
        self.set=set()

    def add(self, key):
        self.set.add(key)

    def remove(self, key):
        if self.contains(key):
            self.set.remove(key)
    def contains(self, key):
        return key in self.set
