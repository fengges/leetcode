class Solution:
    def addToArrayForm(self, A, K):
        B=[int(i) for i in str(K)]
        flag=0
        r=[]
        while A or B:
            a=A.pop() if A else 0
            b=B.pop() if B else 0
            c=a+b+flag
            flag=c//10
            c=c%10
            r.append(c)
        while flag:
            r.append(flag)
            flag=flag//10
        r.reverse()
        return r
s=Solution()
true=True
false=False
test=[
{"input":[[2,7,4],181],"output": [4,5,5]},
{"input":[[1,2,0,0],34],"output": [1,2,3,4]},

]
for t in test:
    r=s.addToArrayForm(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))


