class Solution:
    def findAnagrams(self, s, p):
        tmp={}
        size=len(p)
        if len(s)<size:
            return []
        for i in p:
            if i not in tmp:
                tmp[i]=0
            tmp[i]+=1
        dic={i:0 for i in s}
        for i in range(size):
            dic[s[i]]+=1
        r=[]
        for i in range(len(s)-size+1):
            if self.judge(dic,tmp):
                r.append(i)
            if i==len(s)-size:
                break
            dic[s[i]]-=1
            dic[s[i+size]]+=1
        return r
    def judge(self,dic,tmp):
        for k in dic:
            if k not in tmp and dic[k]>0:
                return False
            elif k in tmp and dic[k]!=tmp[k]:
                return False
        return True

s=Solution()

test=[
{"input":["","a"],"output": []},
{"input":["cbaebabacd","abc"],"output": [0, 6]},

]
for t in test:
    r=s.findAnagrams(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))