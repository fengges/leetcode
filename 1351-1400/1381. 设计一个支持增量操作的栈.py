class CustomStack:

    def __init__(self, maxSize: int):
        self.stack=[]
        self.size=maxSize


    def push(self, x: int) -> None:
        if len(self.stack)<self.size:
            self.stack.append(x)



    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        size=min(k,len(self.stack))
        for i in range(size):
            self.stack[i]+=val


null=None
false=False
true=True
test=[

    {
        "input": {
            'function': ["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"],
            'parm':[[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
        },
        "output":
            [null,null,null,2,null,null,null,null,null,103,202,201,-1]
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
            r = eval("obj." + getCode(function[i], parm[i], 'parm[i]'))
