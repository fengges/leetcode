class Solution:
    def countEven(self, num: int) -> int:
        def fn(n):
            return sum([int(a) for a in str(n)])%2==0

        ans=0
        for i in range(1,num+1):
            if fn(i):
                ans+=1
        return ans
