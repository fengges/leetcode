class MedianFinder:
    def __init__(self):
        self.list=[]

    def addNum(self, num):
        i=len(self.list)
        self.list.append(num)
        for j in range(i,-1,-1):
            # j为当前位置，试探j-1位置
            if num <self.list[j-1]:
                self.list[j] = self.list[j-1]
            else:
                # 位置确定为j
                break
        self.list[j] = num


    def findMedian(self):
        size=len(self.list)
        if size%2==0:
            return (self.list[int(size/2)]+self.list[int(size/2)+1])/2
        else:
            return self.list[int(size/2)]