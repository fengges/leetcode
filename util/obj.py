null=None
false=False
true=True
test=[

    {
        "input": {
            'function': ["Bitset","fix","fix","flip","all","unfix","flip","one","unfix","count","toString"],
            'parm':[[5],[3],[1],[],[],[0],[],[],[0],[],[]]
        },
        "output": [null,null,null,null,false,null,null,true,null,2,"01010"]
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
