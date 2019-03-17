class Solution:
    def isAdditiveNumber(self, num):
        res=[[int(num[0])]]
        for n in range(1,len(num)):
            i=num[n]
            t=int(i)
            res.append([res[-1][0]*10+t])
            size=len(res)-1
            j=0
            while j<size:
                r=res[j]
                if len(r)==1:
                    r.append(t)
                elif len(r)==2:
                    if self.judge(r[0],r[1],t):
                        r.append(t)
                        res.insert(len(res) - 1, [r[0], r[1] * 10 + t])
                    else:
                        r[1]=r[1]*10+t
                else:
                    if r[-1]==r[-2]+r[-3]:
                        if self.judge(r[-1],r[-2],t):
                            r.append(t)
                        else:
                            res.pop(j)
                            j-=1
                            size-=1
                    else:
                        r[-1]=r[-1]*10+t
                        if not self.judge(r[-3],r[-2],r[-1]):
                            res.pop(j)
                            j-=1
                            size-=1
                j+=1
        tmp=[True for r in res if len(r)>=3 and r[-3]+r[-2]==r[-1] and "".join([str(a) for a in r])==num]
        return len(tmp)>0
    def judge(self,r1,r2,t):
        return str(r1+r2).startswith(str(t))
s=Solution()

test=[
{"input":"198019823962","output": True},
{"input":"1023","output": False},
{"input":"199001200","output": False},
{"input": "123","output":True},
{"input": "199100199","output":True},

{"input":"112358","output": True},

]
for t in test:
    r=s.isAdditiveNumber(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
