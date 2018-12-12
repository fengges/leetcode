class Solution:
    one=['Zero',"One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
    ten = ['Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
    hundred = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    def numberToWords(self, num):
        if num==0:
            return "Zero"
        num_s=str(num)
        size=len(num_s)
        r=""
        tmps=["","Thousand","Million","Billion"]
        length=(size-1)//3+1
        start=0
        for i in range(length):
            index=size-3*(length-1-i)
            tmp=self.getEnglish(num_s[start:index])
            if len(tmp)!=0:
                tmp+=" "+tmps[length-i-1]+" "
            r+=tmp
            start=index
        return r.strip()
    def getEnglish(self,num):
        tmp=""
        if len(num)==3:
            if num[0]!="0":
                tmp+=self.one[int(num[0])]+" Hundred "
            num=num[1:]
        if len(num)==2 and num[0]=='1':
             tmp+=self.ten[int(num[-1])]
             return tmp
        elif len(num)==2 and num[0]!='0':
            tmp+=self.hundred[int(num[0])-1]+" "
        if num[-1]!="0":
            return tmp+self.one[int(num[-1])]
        return tmp.strip()
s=Solution()
test=[
{"input":1000000, "output":"One Million"},
{"input":50868, "output":"Fifty Thousand Eight Hundred Sixty Eight"},
{"input": 1000, "output":"One Thousand"},
{"input": 123, "output":"One Hundred Twenty Three"},
{"input": 12345, "output":"Twelve Thousand Three Hundred Forty Five"},
{"input": 1234567, "output":"One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"},
{"input": 1234567891, "output":"One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"},
]

for t in test:
    r=s.numberToWords(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
