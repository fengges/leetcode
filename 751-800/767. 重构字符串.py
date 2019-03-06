class Heap():
    #初始化生成一个优先队列堆
    def __init__(self, elist=[],flag=1,func=None):
        self._elems = list(elist)
        # 1是最小堆 -1是最大堆
        self.flag=flag
        # 自定义函数
        self.func=func

        #初始化时，对数据进行排序
        if elist:
            self.buildheap()

    def buildheap(self):
        end = len(self._elems)
        #所有非叶节点，从后向前进行筛选排序
        for i in range(end//2, -1, -1):
            self.siftdown(self._elems[i], i, end)
    def getValue(self,ele):
        if self.func:
            return self.flag*self.func(ele)
        else:
            return self.flag*ele
    def __len__(self):
        return len(self._elems)
    #向下筛选，使堆按顺序排列
    def siftdown(self,e,begin,end):
        elems, i, j = self._elems, begin, begin*2+1
        while j<end:
            if j+1 < end and self.getValue(elems[j+1]) <self.getValue(elems[j]):
                j += 1
            if self.getValue(e) < self.getValue(elems[j]):
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
    def second(self):
        if len(self._elems)<=1:
            return None,-1
        elif len(self._elems)==2:
            return self._elems[1],1
        else:
            if self._elems[1][1]>=self._elems[2][1]:
                return self._elems[1],1
            else:
                return self._elems[2],2
class Solution(object):
    def reorganizeString(self, S):
        dic={}
        for s in S:
            if s not in dic:
                dic[s]=0
            dic[s]+=1
        r=""
        list=[[k,dic[k]] for k in dic]
        def func(e):
            return e[1]
        t=Heap(list,flag=-1,func=func)
        while True:
            f=t.peek()
            s,index=t.second()
            if f[1]==0:
                break
            if s is None or(s[1]==0 and f[1]>1):
                return ""
            tmp=""
            if s[1]>0:
                tmp=s[0]
                s[1]-=1
                t.siftdown(s, index, len(t))
            if f[1]>0:
                tmp=f[0]+tmp
                f[1]-=1
                t.siftdown(f, 0, len(t))
            r+=tmp
        return r
s=Solution()
test=[

{"input":"bbbbbb", "output":"vlvov"},
{"input":"vvvlo", "output":"vlvov"},
{"input":"aab", "output":"aba"},
{"input":"aaab", "output":""},
]

for t in test:
    r=s.reorganizeString(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))


