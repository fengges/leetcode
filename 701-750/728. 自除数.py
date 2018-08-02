class Solution:
    def selfDividingNumbers(self, left, right):
        result=[]
        for  i in range(left,right+1):
            if self.isZCS(i):
                result.append(i)
        return result
    def isZCS(self,num):
        temp=num
        while temp!=0:
            t=temp%10
            if t!=0 and num%t==0 :
                temp=int(temp/10)
            else:
                return False
        return True

s=Solution()

test=[
{"input":[1,22],"output": [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]},

]
for t in test:
    r=s.selfDividingNumbers(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        # r = s.reverseBetween(t['input'][0], t['input'][1], t['input'][2])