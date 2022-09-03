class Node:
    def __init__(self,user_id,duration):
        self.user_id=user_id
        self.duration=duration
        self.next=None
class SkiRankSystem:
    def __init__(self):
        self.head=Node(-1,float('-inf'))
    def add_record(self,user_id,duration):
        f=self.head
        t=self.head.next
        while t and t.duration<=duration:
            f=t
            t=t.next
        tmp=Node(user_id,duration)
        tmp.next=f.next
        f.next=tmp
    def get_top_athletes(self,num):
        ans=[]
        t=self.head.next
        while len(ans)<num and t:
            if t.user_id not in ans:
                ans.append(t.user_id)
            t=t.next
        return ans
    def quer_top3_record(self,user_id):
        ans=[]
        t=self.head.next
        while len(ans)<3 and t:
            if t.user_id ==user_id:
                ans.append(t.duration)
            t=t.next
        return ans



null=None
false=False
true=True
test=[

    {
        "input": {
            'function': ["SkiRankSystem",'add_record','add_record','get_top_athletes','quer_top3_record'],
            'parm':[[],  [1,10], [2,8],[3],[1]  ]
        },
        "output": [null,null,null,[2,1],[10]]
    },
    {
        "input": {
            'function': ["SkiRankSystem",'add_record','add_record','add_record','get_top_athletes','add_record','add_record','add_record','get_top_athletes','add_record','quer_top3_record','add_record','quer_top3_record'],
            'parm':[[],  [20,8], [22,6],[20,6],[4],[33,5],[22,9],[31,4],[4],[20,8],[20],[20,6],[20]  ]
        },
        "output": [null,null,null,null,[22,20],null,null,null,[31,33,22,20],null,[6,8,8],null,[6,6,8]]
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