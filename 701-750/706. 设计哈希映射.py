class MyHashMap:
    def __init__(self):
        self.dic={}

    def put(self, key, value):
        self.dic[key]=value
    def get(self, key):
        return self.dic.get(key,-1)
    def remove(self, key):
        if key in self.dic:
            del self.dic[key]