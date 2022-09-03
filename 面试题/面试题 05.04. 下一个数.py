class Solution:
    def findClosedNumbers(self, num: int)  :

        def fun(n):
            ans=0
            for a in n:
                ans*=2
                if a=='1':
                    ans+=1
            return ans
        ans=''
        while num:
            ans=str(num%2)+ans
            num//=2
        ans='0'+ans
        index=ans.rfind('1')
        left=ans[0:index].rfind('0')
        right=ans[index+1:].find('0')
        ans1,ans2=-1,-1
        if right>=0:
            right+=index+1
            ans1=ans[0:index]+'0'+ans[index+1:right] +'1' +ans[right+1:]
            ans1=fun(ans1)
        if left>=0:
            ans2=ans[0:left]+'1'+ans[left+1:index] +'0' +ans[index+1:]
            ans2=fun(ans2)
        return [ans2,ans1]

s=Solution()
null=None
test=[
    {"input":67,"output":[2, -1]},
    {"input":2,"output":[4, 1]},
    {"input":1,"output":[2, -1]},

]
for t in test:
    r=s.findClosedNumbers(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))