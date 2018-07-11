class Solution:
    def mySqrt(self, x):
        if x==0:
            return 0
        old=x
        while True:
            new=(old+x/old)/2
            if abs(new-old)<0.001:
                break
            old=new

        return int(new)