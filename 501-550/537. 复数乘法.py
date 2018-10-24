class Solution:
    def complexNumberMultiply(self, a, b):
        one,two=self.computer(a),self.computer(b)
        x,y=one[0]*two[0]-one[1]*two[1],one[0]*two[1]+one[1]*two[0]
        r=str(x)
        if y<0:
            r+="+-"+str(-y)
        else:
            r+='+'+str(y)
        return r+"i"
    def computer(self,a):
        tmp=a[:-1].split('+-')
        if len(tmp)<2:
            tmp=a[:-1].split('+')
        else:
            tmp[1]=-int(tmp[1])
        tmp[0]=int(tmp[0])
        tmp[1]=int(tmp[1])
        return tmp