class Solution:
    def bitwiseComplement(self, num):
        if num==0 :return 1
        n=[]
        while num!=0:
            if num&1==1:
                n.append(1)
            else:
                n.append(0)
            num=num>>1
        n=[1-i for i in n]
        n.reverse()
        r=0
        for i in n:
            r=r*2+i
        return r