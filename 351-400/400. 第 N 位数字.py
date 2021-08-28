class Solution:
    def findNthDigit(self, n: int) -> int:
        ans=9
        size=1
        while True:
            if n<=ans:
                break
            else:
                n-=(ans*size)
                ans*=10
                size+=1

        start=ans//9

        num=n//size
        n=n-num*size
        now=start+num
        return int(str(now)[n%size])
s=Solution()

test=[
    {"input":10,"output":1},
    {"input":9,"output":9},
    {"input":11,"output":0},
    {"input":1,"output":1},
    {"input":3,"output":3},
]

for t in test:
    r=s.findNthDigit(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))





