class Solution:
    def fraction(self, cont)  :
        def fuc2(p, q):
            a,b=max(p,q),min(p,q)
            while b:
                a,b=b,a%b
            return a
        cont.reverse()
        c1=cont.pop(0)
        c2=1
        for c in cont:
            c1,c2=c2,c1
            c1=c1+c*c2
        ans=fuc2(c1,c2)
        return [c1//ans,c2//ans]

s=Solution()

test=[
    {"input":[3, 2, 0, 2],"output":[13,4]},
    {"input":[2147483647],"output":[13,4]},


]
for t in test:
    r=s.fraction(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))



