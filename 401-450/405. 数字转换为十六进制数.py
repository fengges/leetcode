class Solution:
    def toHex(self, num):
        tmp=[0 for i in range(32)]
        for i in range(32):
            if num&1==1:
                tmp[i]=1
            num=num>>1
        tmp.reverse()
        dic={10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
        s=""
        for i in range(0,32,4):
            sum=tmp[i]*8+tmp[i+1]*4+tmp[i+2]*2+tmp[i+3]
            if sum>=10:
                s+=dic[sum]
            else:
                s+=str(sum)
        s=s.lstrip("0")
        if len(s)==0:
            return "0"
        else:
            return s
