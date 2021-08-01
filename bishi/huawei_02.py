
class Solution:
    def __init__(self,size):
        self.arr=[]
        self.size=size
    def next(self, val):
        self.arr.append(val)
        if len(self.arr)>self.size:
            self.arr.pop(0)
        return sum(self.arr)/len(self.arr)

null=None
test=[
    {
        "input": {
            'function': ["Solution","next","next","next","next","next"],
            'parm': [[3],[1],[10],[3],[5],[6]]
        },
        "output": [null,1,5.5,4.6,5,55,5]
    },
    # {
    #     "input":{
    #         'function':["MyCalendarThree","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book"],
    #         'parm':[[],[47,50],[1,10],[27,36],[40,47],[20,27],[15,23],[10,18],[27,36],[17,25],[8,17],[24,33],[23,28],[21,27],[47,50],[14,21],[26,32],[16,21],[2,7],[24,33],[6,13],[44,50],[33,39],[30,36],[6,15],[21,27],[49,50],[38,45],[4,12],[46,50],[13,21]]
    #     },
    #     "output": [null,1,1,1,1,1,2,2,2,3,3,3,4,5,5,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,7]
    # },
]
def getCode(function,param,name):
    return function+"("+",".join([name+"["+str(i)+"]" for i in range(len(param))]) +")"
for t in test:
    function=t['input']['function']
    parm=t['input']['parm']
    output = t['output']
    obj=eval(getCode(function[0],parm[0],""))
    for i in range(1,len(function)):
        r=eval("obj."+getCode(function[i], parm[i],'parm[i]'))
        if r!=output[i]:
            print("error")
            r = eval("obj." + getCode(function[i], parm[i], 'parm[i]'))