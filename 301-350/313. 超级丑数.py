class Solution:
    def nthSuperUglyNumber(self, n, primes):
        t=[0 for i in primes]
        result=[1]
        while n!=len(result):
            temp=[primes[i]*result[t[i]] for i in range(len(primes))]
            new=min(temp)
            result.append(new)
            for i,v in enumerate(temp):
                if v==new:
                    t[i]+=1
        return result[-1]