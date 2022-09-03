class Solution:
    def translateNum(self, num: int) -> int:
        str_num=str(num)
        str_num='0'+str_num
        flag=[0 for i in range(len(str_num))]
        flag[0]=1
        flag[1]=1
        for i in range(2,len(flag)):
            flag[i]+=flag[i-1]
            if  str_num[i-1:i+1]<='25' and str_num[i-1]!='0' :
                flag[i]+=flag[i-2]
        return flag[-1]


s=Solution()
test=[
    {"input":506, "output":1},
    {"input":26, "output":1},
    {"input":25, "output":2},
]

for t in test:
    r=s.translateNum(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.translateNum(t['input'])
