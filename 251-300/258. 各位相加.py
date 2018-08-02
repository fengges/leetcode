class Solution:
    def addDigits(self, num):
        while num<10:
            sum=0
            s=str(num)
            for i in s:
                sum+=int(i)
            num=sum
        return num