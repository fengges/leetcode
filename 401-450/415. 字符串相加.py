class Solution:
    def addStrings(self, num1, num2):
        a=[int(i) for i in num1]
        b=[int(i) for i in num2]
        a.reverse()
        b.reverse()
        length=max(len(a),len(b))+1
        for i in range(len(a),length):
            a.append(0)
        for i in range(len(b),length):
            b.append(0)
        flag=0
        for i in range(len(a)):
            t=a[i]+b[i]+flag
            if t>=10:
                flag=int(t/10)
                t=t%10
            else:
                flag=0
            a[i]=t
        if a[-1]==0:
            del a[-1]
        a=[str(i) for i in a]
        a.reverse()
        return "".join(a)
