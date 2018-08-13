class Solution:
    def evalRPN(self, tokens):
        stack=[]
        for t in tokens:
            if  self.isNumber(t):
                stack.append(int(t))
            else:
                self.computer(stack,t)
        return stack[0]
    def isNumber(self,t):
        try :
            int(t)
            return True
        except:
            return False
    def computer(self, v_stack, c):
        b = v_stack.pop()
        a = v_stack.pop()
        if c == "+":
            v = a + b
        elif c == "-":
            v = a - b
        elif c == '*':
            v = a * b
        else:
            v = int(a / b)
        v_stack.append(v)

s=Solution()
test=[
{"input": ["10","6","9","3","+","-11","*","/","*","17","+","5","+"], "output":2},
]

for t in test:
    r=s.evalRPN(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.evalRPN(t['input'])