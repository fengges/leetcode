class Solution:
    def integerReplacement(self, n):
        dic=set()
        last={1}
        level=0
        dic.add(1)
        while n not in last:
            level+=1
            tmp=set()
            for i in last:
                if i-1>0 and i-1 not in dic:
                    dic.add(i-1)
                    tmp.add(i-1)
                if i+1<2*n+1 and i+1 not in dic:
                    dic.add(i + 1)
                    tmp.add(i+1)
                if  i<n and 2*i not in dic:
                    dic.add(2*i)
                    tmp.add(2*i)
            last=tmp
        return level
s=Solution()

test=[
{"input":1234,"output": 2},
{"input":100000000,"output": 2},
{"input":7,"output": 4},
{"input":8,"output": 3},
]
for t in test:
    r=s.integerReplacement(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))



