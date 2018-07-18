class Solution:
    def restoreIpAddresses(self, s):
        self.result=[]
        self.find([],s,4)
        return self.result
    def find(self,list,s,num):
        if num==1:
            if len(s)>0 and int(s)<=255 and len(s)==len(str(int(s))) :
                self.result.append(".".join(list)+'.'+s)

            return
        if len(s)>=3 and int(s[0:3])<=255 and len(str(int(s[0:3])))==3:
            list.append(s[0:3])
            self.find(list,s[3:],num-1)
            del list[-1]
        if len(s)>=2 and len(str(int(s[0:2])))==2:
            list.append(s[0:2])
            self.find(list,s[2:],num-1)
            del list[-1]
        if len(s)>=1 :
            list.append(s[0:1])
            self.find(list,s[1:],num-1)
            del list[-1]
        return

s=Solution()
test=[

{"input":"010010", "output": ["255.255.11.135", "255.255.111.35"]},
{"input":"0000", "output": ["255.255.11.135", "255.255.111.35"]},
{"input":"25525511135", "output": ["255.255.11.135", "255.255.111.35"]},

]

for t in test:
    r=s.restoreIpAddresses(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.restoreIpAddresses(t['input'])
