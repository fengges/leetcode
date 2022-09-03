class Solution:
    def findNthDigit(self, n: int) -> int:
            # write code here
            if n<10:
                return n
            n10=2
            n-=10
            while True:
                number=9*10**(n10-1)
                if n>=number*n10:
                    n-=number*n10
                    n10+=1
                else:
                    break
            size=10**(n10-1)+n//(n10)

            return  int(str(size)[n%(n10)])
s=Solution()

test=[
    {"input":100,"output":5},
    {"input":11,"output":0},
    # {"input":500000000,"output":1},
    {"input":10,"output":1},
    {"input":9,"output":9},

    {"input":1,"output":1},
    {"input":3,"output":3},
]

for t in test:
    r=s.findNthDigit(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))





