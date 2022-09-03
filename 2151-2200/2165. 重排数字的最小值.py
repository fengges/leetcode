class Solution:
    def smallestNumber(self, num: int) -> int:

        flag=num>=0
        num=abs(num)

        ans=[a for a in str(num)]
        if flag:
            ans.sort()
            f='0'
            for a in ans:
                if a!='0':
                    f=a
                    break
            index=ans.index(f)
            return int(f+''.join(ans[0:index])+''.join(ans[index+1:]))
        else:
            ans.sort(reverse=True)
            return int('-'+''.join(ans))
s=Solution()
null=None
test=[
    {"input":0,"output":0},
    {"input":310,"output":103},
    {"input":-7605,"output":-7650},

]
for t in test:
    r=s.smallestNumber(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))