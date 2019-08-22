class Solution:
    def smallestRepunitDivByK(self, K):
        if K%2==0 or K%5==0:
            return -1
        result=1
        yu=1
        all=1
        while all%K!=0:
            yu=(yu*10)%K
            all+=yu
            result+=1
        return result