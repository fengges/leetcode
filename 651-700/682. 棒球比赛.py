class Solution:
    def calPoints(self, ops):
        num=[]
        for i in ops:
           if i=='C':
                del num[-1]
           elif i=="D":
                num.append(num[-1]*2)
           elif i=="+":
               num.append(num[-1] +num[-2])
           else:
               num.append(int(i))
        return sum(num)