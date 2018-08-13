class Solution:
    def calculate(self, s):
        lists=[]
        i=0
        while i<len(s) :
            if ord(s[i])>=ord('0') and ord(s[i])<=ord('9'):
                if len(lists)==0 or lists[-1]["type"]==False:
                    lists.append({'value':int(s[i]), "type":True})
                else:
                    lists[-1]['value']=lists[-1]['value']*10+int(s[i])
            elif s[i]!=' ':
                lists.append({'value':s[i],"type":False})
            i+=1
        c_stack=[]
        v_stack = []
        for l in lists:
            if l["type"]:
                v_stack.append(l['value'])
            elif len(c_stack)==0 or l['value']=='(':
                c_stack.append(l['value'])
            elif l['value']!=")" and self.cmp(c_stack[-1],l['value'])>0:
                c_stack.append(l['value'])
            elif l['value']==')':
                while True:
                    c = c_stack.pop()
                    if c=="(":
                        break
                    self.computer(v_stack,c)
            else:
                while len(c_stack)>0 and self.cmp(c_stack[-1],l['value'])<=0:
                    c=c_stack.pop()
                    self.computer(v_stack,c)
                c_stack.append(l['value'])

        while True:
            if len(c_stack)==0:
                break
            c = c_stack.pop()
            self.computer(v_stack, c)

        return v_stack[0]
    def computer(self,v_stack,c):
        b = v_stack.pop()
        a = v_stack.pop()
        if c == "+":
            v = a + b
        elif c == "-":
            v = a - b
        elif c == '*':
            v = a * b
        else:
            v = a / b
        v_stack.append(v)
    def cmp(self,op1,op2):
        dic={'-':1,'+':1,'*':2,'/':2,'(':0}
        return dic[op2]-dic[op1]
s=Solution()
test=[
{"input":  "1*2-3/4+5*6-7*8+9/10", "output":-24},
{"input": "1 + 1", "output":2},
{"input":  " 2-1 + 2 ", "output":3},
{"input":  "(1+(4+5+2)-3)+(6+8)", "output":23},
]

for t in test:
    r=s.calculate(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.calculate(t['input'])