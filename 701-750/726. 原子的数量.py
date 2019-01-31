class Solution:
    def countOfAtoms(self, formula):
        size=len(formula)
        dic={}
        stack=[{}]
        i=0
        last=None
        while i<size:
            if formula[i]==")":
                num=0
                while i+1<size and formula[i+1].isdigit():
                    num=num*10+int(formula[i+1])
                    i+=1
                tmp=stack[-1]
                stack.pop()
                for k in tmp:
                    if k not in stack[-1]:
                        stack[-1][k] = 0
                    stack[-1][k] += num*tmp[k]
            elif formula[i]=="(":
                stack.append({})
            elif ord(formula[i])>=ord('a') and ord(formula[i])<=ord('z'):
                stack[-1][last+formula[i]]=stack[-1][last]
                stack[-1].pop(last)
                last = last+formula[i]
            elif formula[i].isdigit():
                num=int(formula[i])
                while i+1<size and formula[i+1].isdigit():
                    num=num*10+int(formula[i+1])
                    i+=1
                stack[-1][last]=stack[-1][last]*num
            else:
                last=formula[i]
                if last not in stack[-1]:
                    stack[-1][last]=0
                stack[-1][last]+=1
            i+=1
        for r in stack:
            for t in r:
                if t not in dic:
                    dic[t]=0
                dic[t]+=r[t]
        result=sorted(dic.items(),key=lambda x:x[0])
        return ''.join([r[0]+str(r[1]) if r[1]!=1 else r[0]+''  for r in result])

s=Solution()
test=[
{"input": "H11He49NO35B7N46Li20", "output":181},
{"input": "Be32", "output":181},
{"input": "K4(ON(SO3)2)2", "output":181},
{"input":"Mg(OH)2", "output":181},
{"input": "H2O", "output":181},


]

for t in test:
    r=s.countOfAtoms(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
