class Link:
    def __init__(self,k,v):
        self.next=None
        self.pre=None
        self.val=v
        self.key=k
class LRUCache:

    def __init__(self, capacity: int):
        self.maxSize=capacity
        self.size=0
        self.head=Link(-1,-1)
        self.tail=Link(-1,-1)
        self.head.next=self.tail
        self.tail.pre=self.head
        self.dicts={}
    def get(self, key: int) -> int:
        if key in self.dicts:
            val=self.dicts[key].val
            self.put(key,val)
            return val
        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.dicts:
            tmp=self.dicts[key]
            tmp.val=value
            # 从链表中删除
            tmp.pre.next=tmp.next
            tmp.next.pre=tmp.pre
            self.dicts.pop(tmp.key)
        else:
            if self.size>=self.maxSize:

                tmp=self.tail.pre
                # 从链表中删除
                tmp.pre.next=tmp.next
                tmp.next.pre=tmp.pre
                self.dicts.pop(tmp.key)
            else:
                self.size+=1
        # 插入第一个
        t=Link(key,value)
        self.dicts[key]=t
        t.next=self.head.next
        t.pre=self.head
        self.head.next=t
        t.next.pre=t
def func(obj):
    arr=[]
    node=obj.head
    while node:
        arr.append(node.val)
        node=node.next
    node=obj.tail
    arr2=[]
    while node:
        arr2.append(node.val)
        node=node.pre
    return arr,arr2
pass
null=None
false=False
true=True
test=[
    {
        "input": {
            'function':
                ["LRUCache","put","put","get","put","get","put","get","get","get"],
            'parm':[[2],[1,0],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
        },
        "output": [[2],[1,0],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
    },
    {
        "input": {
            'function':
                ["LRUCache","put","get"],
            'parm':[[1],[2,1],[2]]
        },
        "output": [null,null,1]
    },
    {
        "input": {
            'function':
                ["LRUCache","put","put","get","put","get","put","get","get","get"],
            'parm':[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
        },
        "output": [null,null,null,1,null,-1,null,-1,3,4]
    },

]
def getCode(function,param,name):
    return function+"("+",".join([name+"["+str(i)+"]" for i in range(len(param))]) +")"
for t in test:
    function=t['input']['function']
    parm=t['input']['parm']
    output = t['output']
    obj=eval(getCode(function[0],parm[0],"parm[0]"))
    for i in range(1,len(function)):
        r=eval("obj."+getCode(function[i], parm[i],'parm[i]'))
        if r!=output[i]:
            print("error")
            # r = eval("obj." + getCode(function[i], parm[i], 'parm[i]'))

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)