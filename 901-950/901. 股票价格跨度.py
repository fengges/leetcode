class StockSpanner:
    def __init__(self):
        self.list=[]
    def next(self, price) :
        self.list.append(price)
        size=len(self.list)
        r=0
        for i in range(size-1,-1,-1):
            if self.list[i]<=price:
                r+=1
            else:
                break
        return r

