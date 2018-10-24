class Solution(object):
    def convertToBase7(self, num):
        flag=True
        if num<0:
            flag=False
            num=-num
        r=[]
        base=7
        while num!=0:
            r.append(str(num%base))
            num=int(num/base)
        r.reverse()
        tmp=''.join(r)
        if len(tmp)==0:
            tmp="0"
        if flag is False:
            tmp='-'+tmp
        return tmp
