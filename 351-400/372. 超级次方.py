class Solution:
    def superPow(self, a, b):
        if len(b)==0:
            return 1
        tmp=1337
        b.reverse()
        r=1
        for i in b:
            r=pow(a,i,tmp)*r%tmp
            a=pow(a,10,tmp)
        return r
    def pow(self,a,b,c):
        r=1
        for i in range(b):
            r=r*a%c
        return r
