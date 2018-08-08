class Solution:
    def isHappy(self, n):
        dic={}
        while n!=1:
            if n in dic:
                return False
            s=str(n)
            dic[n]=1
            n=0
            for i in s:
                n+=int(i)*int(i)
        return True
s=Solution()

test=[

{"input":1,"output":True},

]


for t in test:
    r=s.isHappy(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
