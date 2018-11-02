class Solution:
    def numUniqueEmails(self, emails):
        dic={}
        for email in emails:
            tmp=email.split('@')
            tmp[0]=tmp[0].replace('.',"")
            index=tmp[0].find('+')
            if index>=0:
                tmp[0]=tmp[0][0:index]
            dic[tmp[0]+"@"+tmp[1]]=1
        return len(dic)

s=Solution()
test=[
{"input":  ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"],"output":2},
]

for t in test:
    r=s.numUniqueEmails(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))