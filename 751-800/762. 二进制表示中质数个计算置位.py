class Solution(object):
    def countPrimeSetBits(self, L, R):
        r=0
        dic={}
        for i in range(L,R+1):
            n=self.count(i)
            if n not in dic:
                dic[n]=self.isPrime(n)
            if dic[n]:
                r += 1
        return r

    def isPrime(self,n):
        if n <= 1:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True
    def count(self,n):
        sum=0
        while n!=0:
            if n&1==1:
                sum+=1
            n=n>>1
        return sum

s=Solution()
test=[
{"input": [842,888], "output":["0->2","4->5","7"]},
]

for t in test:
    r=s.countPrimeSetBits(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.countPrimeSetBits(t['input'][0], t['input'][1])