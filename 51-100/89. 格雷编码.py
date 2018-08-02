class Solution:
    def grayCode(self, n):
        sum=1
        list=[1]

        for i in range(1,n):
            sum*=2
            list.append(sum)
        result=[]
        
        print(list)

s=Solution()
test=[
{"input": 2, "output":[0,1,3,2]},
]

for t in test:
    r=s.grayCode(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.grayCode(t['input'])