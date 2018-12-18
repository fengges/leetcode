class Solution:
    def countOfAtoms(self, formula):
        size=len(formula)
        dic={}
        stack=[]
        i=0
        while i<size:
            if formula[i]==")":
                num=0
                while i+1<size and formula[i+1].isdigit():
                    num=num*10+int(formula[i+1])
                    i+=1
                tmp=[]
                while stack[-1]!="(":
                    tmp.append(stack[-1])
                    stack.pop()
                stack.pop()
                tmp.reverse()
                stack.append(' '.join(tmp*num))
            elif ord(formula[i])>=ord('a') and ord(formula[i])<=ord('z'):
                stack[-1]+=formula[i]
            elif formula[i].isdigit():
                num=int(formula[i])
                while i+1<size and formula[i+1].isdigit():
                    num=num*10+int(formula[i+1])
                    i+=1
                tmp=" ".join([stack[-1]]*num)
                stack[-1]=tmp
            else:
                stack.append(formula[i])
            i+=1
        r=" ".join(stack).split(' ')
        for t in r:
            if t not in dic:
                dic[t]=0
            dic[t]+=1
        result=sorted(dic.items(),key=lambda x:x[0])
        return ''.join([r[0]+str(r[1]) if r[1]!=1 else r[0]+''  for r in result])

s=Solution()
test=[
{"input": "H2O", "output":181},
{"input":"Mg(OH)2", "output":181},
{"input": "K4(ON(SO3)2)2", "output":181},
]

for t in test:
    r=s.countOfAtoms(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
