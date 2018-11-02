class Solution:
    def findLongestWord(self, s, d):
        r=[]
        m=1
        for w in d:
            t=self.count(s,w)
            if t>m:
                m=t
                r=[w]
            elif  t==m:
                r.append(w)
        r.sort()
        if len(r)==0:
            return ""
        return r[0]
    def count(self,a,b):
        if len(a)<len(b):
            return -1
        b_i=0
        for i in range(len(a)):
            if a[i]==b[b_i]:
                b_i+=1
            if b_i==len(b):
                return len(b)
        return -1

s=Solution()

test=[
{"input":  ["aaa",["aaa","aa","a"]],"output":"aaa"},
{"input":  ["abpcplea",["a","b","c"]],"output":"a"},
{"input":  ["apple",["zxc","vbn"]],"output":""},
{"input":  ["abpcplea",["ale","apple","monkey","plea"]],"output":"apple"},

]

for t in test:
    r=s.findLongestWord(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))