
null=None
test=[
    {
        "input": {
            'function': ["MyCalendarThree","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book"],
            'parm': [[],[89,100],[30,43],[92,100],[31,49],[59,76],[60,73],[31,49],[80,99],[48,60],[36,52],[67,82],[96,100],[22,35],[18,32],[9,24],[11,27],[94,100],[12,22],[61,74],[3,20],[14,28],[27,37],[5,20],[1,11],[96,100],[33,44],[90,100],[40,54],[23,35],[18,32],[78,89],[56,66],[83,93],[45,59],[40,59],[94,100],[99,100],[86,96],[43,61],[29,45],[21,36],[13,31],[17,30],[16,30],[80,94],[38,50],[15,30],[62,79],[25,39],[73,85],[39,56],[80,97],[42,57],[32,47],[59,78],[35,53],[56,74],[75,85],[39,54],[63,82]]
        },
        "output": [null,1,1,2,2,2,2,3,3,3,4,4,4,4,5,5,5,5,5,5,5,6,6,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,8,8,9,10,10,10,11,11,11,12,12,12,12,12,12,12,12,12,13,13,13,14,14]
    },
    {
        "input":{
            'function':["MyCalendarThree","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book"],
            'parm':[[],[47,50],[1,10],[27,36],[40,47],[20,27],[15,23],[10,18],[27,36],[17,25],[8,17],[24,33],[23,28],[21,27],[47,50],[14,21],[26,32],[16,21],[2,7],[24,33],[6,13],[44,50],[33,39],[30,36],[6,15],[21,27],[49,50],[38,45],[4,12],[46,50],[13,21]]
        },
        "output": [null,1,1,1,1,1,2,2,2,3,3,3,4,5,5,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,7]
    },
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
