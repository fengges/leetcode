class Solution(object):
    def hammingWeight(self, n):
        num=0
        while n!=0:
            if n%2==1:
                num+=1
            n=int(n/2)
        return num