class Heap2():
    # 初始化生成一个优先队列堆
    def __init__(self, elist=[], flag=1, func=None):
        self._elems = list(elist)
        # 1是最小堆 -1是最大堆
        self.flag = flag
        # 自定义函数
        self.func = func

        # 初始化时，对数据进行排序
        if elist:
            self.buildheap()

    def buildheap(self):
        end = len(self._elems)
        # 所有非叶节点，从后向前进行筛选排序
        for i in range(end // 2, -1, -1):
            self.siftdown(self._elems[i], i, end)

    def getValue(self, ele):
        if self.func:
            return self.flag * self.func(ele)
        else:
            return self.flag * ele

    def __len__(self):
        return len(self._elems)

    # 向下筛选，使堆按顺序排列
    def siftdown(self, e, begin, end):
        elems, i, j = self._elems, begin, begin * 2 + 1
        while j < end:
            if j + 1 < end and self.getValue(elems[j + 1]) < self.getValue(elems[j]):
                j += 1
            if self.getValue(e) < self.getValue(elems[j]):
                break
            elems[i] = elems[j]
            i, j = j, 2 * j + 1
        elems[i] = e

    # 检测收否为空
    def is_empty(self):
        return not self._elems

    # 返回顶峰值
    def peek(self):
        if self.is_empty():
            raise PermissionError("in peek")
        return self._elems[0]

    def second(self):
        if len(self._elems) <= 1:
            return None, -1
        elif len(self._elems) == 2:
            return self._elems[1], 1
        else:
            if self._elems[1][1] >= self._elems[2][1]:
                return self._elems[1], 1
            else:
                return self._elems[2], 2


class Heap():
    #初始化生成一个优先队列堆
    def __init__(self, elist=[],flag=1):
        self._elems = list(elist)
        self.flag=flag
        # 1是最小堆 -1是最大堆
        #初始化时，对数据进行排序
        if elist:
            self.buildheap()

    def buildheap(self):
        end = len(self._elems)
        #所有非叶节点，从后向前进行筛选排序
        for i in range(end//2, -1, -1):
            self.siftdown(self._elems[i], i, end)

    #向下筛选，使堆按顺序排列
    def siftdown(self,e,begin,end):
        elems, i, j = self._elems, begin, begin*2+1
        while j<end:
            if j+1 < end and self.flag*elems[j+1] <self.flag* elems[j]:
                j += 1
            if self.flag*e < self.flag*elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, 2*j+1
        elems[i] = e

    #检测收否为空
    def is_empty(self):
        return not self._elems

    #返回顶峰值
    def peek(self):
        if self.is_empty():
            raise PermissionError("in peek")
        return self._elems[0]

class PrioQueue():
    """implementing priority queues using heaps
    """

    #初始化生成一个优先队列堆
    def __init__(self, elist=[],flag=1):
        self._elems = list(elist)
        #初始化时，对数据进行排序
        self.flag=flag
        # 1是最小堆 -1是最大堆
        if elist:
            self.buildheap()


    #生成堆的函数
    def buildheap(self):
        end = len(self._elems)
        #所有非叶节点，从后向前进行筛选排序
        for i in range(end//2, -1, -1):
            self.siftdown(self._elems[i], i, end)


    #向下筛选，使堆按顺序排列
    def siftdown(self,e,begin,end):
        elems, i, j = self._elems, begin, begin*2+1
        while j<end:
            if j+1 < end and self.flag*elems[j+1] <self.flag*elems[j]:
                j += 1
            if self.flag*e <self.flag* elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, 2*j+1
        elems[i] = e

    #弹出元素，之后利用sifidown恢复顺序
    def dequeue(self):
        if self.is_empty():
            raise ("in dequeue")
        elems = self._elems
        #取出第一个即优先级最高的元素
        e0 = elems[0]
        #弹出最后一个元素再放向下筛选函数中进行筛选
        e = elems.pop()
        if len(elems) > 0:
            #用e表示0位置的值，代替了本该是头部位置的数，相当于把这个数给除去了
            self.siftdown(e,0,len(elems))
        return e0

    #插入元素，使用向上筛选进行排序
    def enqueue(self,e):
        self._elems.append(None)
        self.siftup(e, len(self._elems)-1)
    #向上筛选，恢复顺序
    def siftup(self, e, last):
        elems, i, j = self._elems, last, (last-1)//2
        while i > 0 and self.flag*e <self.flag* elems[j]:
            elems[i] = elems[j]
            i, j = j, (j-1)//2
        elems[i] = e

    #检测收否为空
    def is_empty(self):
        return not self._elems

    #返回顶峰值
    def peek(self):
        if self.is_empty():
            raise PermissionError("in peek")
        return self._elems[0]

class PrioQueue2():
    """implementing priority queues using heaps
    """

    #初始化生成一个优先队列堆
    def __init__(self,cmp=None,elist=[]):
        self._elems = list(elist)
        #初始化时，对数据进行排序
        if cmp:
            self.cmp=cmp
        else:
            def cmp(a,b):
                return a>b
            self.cmp=cmp


        # 1是最小堆 -1是最大堆
        if elist:
            self.buildheap()

    #生成堆的函数
    def buildheap(self):
        end = len(self._elems)
        #所有非叶节点，从后向前进行筛选排序
        for i in range(end//2, -1, -1):
            self.siftdown(self._elems[i], i, end)


    #向下筛选，使堆按顺序排列
    def siftdown(self,e,begin,end):
        elems, i, j = self._elems, begin, begin*2+1
        while j<end:
            if j+1 < end and self.cmp(elems[j+1] ,elems[j]):
                j += 1
            if self.cmp(e , elems[j]):
                break
            elems[i] = elems[j]
            i, j = j, 2*j+1
        elems[i] = e

    #弹出元素，之后利用sifidown恢复顺序
    def dequeue(self):
        if self.is_empty():
            raise ("in dequeue")
        elems = self._elems
        #取出第一个即优先级最高的元素
        e0 = elems[0]
        #弹出最后一个元素再放向下筛选函数中进行筛选
        e = elems.pop()
        if len(elems) > 0:
            #用e表示0位置的值，代替了本该是头部位置的数，相当于把这个数给除去了
            self.siftdown(e,0,len(elems))
        return e0

    #插入元素，使用向上筛选进行排序
    def enqueue(self,e):
        self._elems.append(None)
        self.siftup(e, len(self._elems)-1)
    #向上筛选，恢复顺序
    def siftup(self, e, last):
        elems, i, j = self._elems, last, (last-1)//2
        while i > 0 and self.cmp(e , elems[j]):
            elems[i] = elems[j]
            i, j = j, (j-1)//2
        elems[i] = e

    #检测收否为空
    def is_empty(self):
        return not self._elems

    #返回顶峰值
    def peek(self):
        if self.is_empty():
            raise PermissionError("in peek")
        return self._elems[0]

if __name__=="__main__":
    t=PrioQueue([1,2,3,4,5],-1)
    t.enqueue(5)


