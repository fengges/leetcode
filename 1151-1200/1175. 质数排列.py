class Solution:
    def numPrimeArrangements(self, n):

        self.mod = 1000000007

        prims=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        count= 0
        for i in range(len(prims)):
            if prims[i] <= n:
                count+=1
            else:
                break

        return (self.A(count) * self.A(n - count)) % self.mod


    def A(self,x):
        sum= 1
        for i in range(2,x+1):
            sum = (sum * i) % self.mod
        return sum

