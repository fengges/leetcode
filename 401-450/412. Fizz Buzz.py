class Solution:
    def fizzBuzz(self, n):
        r=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                r.append("FizzBuzz")
            elif i%5==0:
                r.append("Buzz")
            elif i%3==0:
                r.append("Fizz")
            else:
                r.append(str(i))
        return r
