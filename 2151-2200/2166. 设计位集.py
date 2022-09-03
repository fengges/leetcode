class Bitset:

    def __init__(self, size: int):
        self.size=size
        self.num=0
        self.ans=['0' for i in range(size)]

    def fix(self, idx: int) -> None:
        if self.ans[idx]=='0':
            self.ans[idx]='1'
            self.num+=1

    def unfix(self, idx: int) -> None:
        if self.ans[idx]=='1':
            self.ans[idx]='0'
            self.num-=1

    def flip(self) -> None:
        self.ans=['1' if a=='0' else '0' for a in self.ans]
        self.num=self.size-self.num
    def all(self) -> bool:
        return self.num==self.size

    def one(self) -> bool:
        return self.num>0

    def count(self) -> int:
        return self.num

    def toString(self) -> str:
        return ''.join(self.ans)
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

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()