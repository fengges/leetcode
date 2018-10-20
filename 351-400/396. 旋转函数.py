
class Solution:
    def maxRotateFunction(self, A):
        sum ,temp = 0,0
        size =len(A)
        for i in range(size):
            sum += A[i]
            temp += i * A[i]
        r = temp
        for i in range(1,size):
            pos = size - i
            temp = sum + temp - size * A[pos]
            r = max(r,temp)
        return r
s=Solution()
test=[
{"input":[-2147483648,-2147483648], "output":26},
{"input":[4, 3, 2, 6], "output":26},
]

for t in test:
    r=s.maxRotateFunction(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))