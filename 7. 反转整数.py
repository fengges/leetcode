class Solution:
    def reverse(self, x):
        zheng=True
        if x<0:
            zheng=False
            x=-x
        elif x==0:
            return 0
        s=''
        while x>0:
            s+=str(x%10)
            x=int(x/10)
        s=int(s)
        if not zheng:
            if s>2147483648:
                return 0
            else:
                return -s
        else:
            if s>2147483647:
                return 0
            else:
                return s



s=Solution()

test=[
{"input":0,"output":0},
{"input":123,"output":321},
{"input":-123,"output":-321},
{"input":120,"output":21},

      ]

for t in test:
    r=s.reverse(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.reverse(t['input'])