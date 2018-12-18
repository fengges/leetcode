import math
class Solution:
    def primePalindrome(self, N):
        if (N <= 11):
            if (N <= 2):
                return 2
            elif (N == 3):
                return 3
            elif (N <= 5):
                return 5
            elif (N <= 7):
                return 7
            else:
                return 11
        else:
            while True:
                size=len(str(N))
                if size%2==0:
                    N=int("1"+''.join(['0' for i in range(size)]))+1
                elif self.isPalindrome(str(N)):
                    if self.isPrime(N):
                        break
                    else:
                        N+=2
                else:
                    N+=1
            return N

    def isPrime1(self,n):
        if n <= 1:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True
    def isPrime(self,num):
        sqrt = int(num/2)

        for i in range(5,sqrt+1,6):
            if (num % i == 0 or num % (i + 2) == 0):
                return False
        return True
    def isPalindrome(self,nums):
       size=len(nums)
       for i in range(int(size/2)):
            if (nums[i] != nums[size - i - 1]):
                return False
       return True


s=Solution()
test=[
{"input": 9932400, "output":181},
{"input": 7778778, "output":181},
{"input": 181, "output":181},
{"input": 33, "output":101},
]

for t in test:
    r=s.primePalindrome(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))