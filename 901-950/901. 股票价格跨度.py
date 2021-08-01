class StockSpanner:
    def __init__(self):
        self.arr=[]
        self.ans=[]
    def next(self, price) :

        size=len(self.arr)
        def func(index):
            if index==-1:
                return -1
            if price<self.arr[index]:
                return index
            else:
                return func(index-self.ans[index])
        r=func(size-1)
        self.arr.append(price)
        self.ans.append(size-r)
        return self.ans[-1]

null = None
test = [
    {
        "input": {
            'function': ["StockSpanner","next","next","next","next","next","next","next"],
            'parm': [[],[100],[80],[60],[70],[60],[75],[85]]
        },
        "output": [null,1,1,1,2,1,4,6]
    },
]


def getCode(function, param, name):
    return function + "(" + ",".join([name + "[" + str(i) + "]" for i in range(len(param))]) + ")"


for t in test:
    function = t['input']['function']
    parm = t['input']['parm']
    output = t['output']
    obj = eval(getCode(function[0], parm[0], ""))
    for i in range(1, len(function)):
        r = eval("obj." + getCode(function[i], parm[i], 'parm[i]'))
        if r != output[i]:
            print("error")
            r = eval("obj." + getCode(function[i], parm[i], 'parm[i]'))
            print(r)
