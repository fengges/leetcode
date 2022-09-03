# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param lists ListNode类一维数组
# @return ListNode类
#
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
                return 1 if a>=b else -1
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
            if j+1 < end and self.cmp(elems[j+1] ,elems[j])>=0:
                j += 1
            if self.cmp(e , elems[j])>=0:
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
        while i > 0 and self.cmp(e , elems[j])>=0:
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

class Solution:
    def mergeKLists(self , lists ) -> ListNode:

        # write code here
        lists=[l for l in lists if l]
        def cmp(a,b):
            if a.val==b.val: return 0
            return -1 if a.val>b.val else 1
        heap=PrioQueue2(cmp,lists)
        head=ListNode(-1)
        tail=head
        while not heap.is_empty():
            t=heap.dequeue()
            tail.next=t
            tail=t
            if t.next:
                heap.enqueue(t.next)

        return head.next
s=Solution()

test=[
    {"input":[toLinkNode([10,12]),toLinkNode([1,4,5]),toLinkNode([6])],"output":2},

]
for t in test:
    r=s.mergeKLists(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))