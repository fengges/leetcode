class LRUCache:
    def __init__(self, capacity):
        self.que=[]
        self.size=capacity
        self.dic={}

    def get(self, key):
        if key in self.dic:
            self.que.remove(key)
            self.que.insert(0,key)
            return self.dic[key]
        return -1

    def put(self, key, value):
        if key in self.dic:
            self.que.remove(key)
            self.que.insert(0,key)
            self.dic[key] = value
            return
        elif len(self.que)>=self.size:
            tmp=self.que[-1]
            del self.que[-1]
            del self.dic[tmp]
        self.que.insert(0,key)
        self.dic[key]=value