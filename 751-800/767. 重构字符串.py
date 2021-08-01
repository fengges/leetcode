
class Solution(object):
    def reorganizeString(self, S):
        dic={}
        for s in S:
            if s not in dic:
                dic[s]=0
            dic[s]+=1
        r=""
        list=[[k,dic[k]] for k in dic]
        if len(list)==1:
            if len(S)==1:
                return S
            else:
                return ''
        while True:
            list.sort(key=lambda x:x[1],reverse=True)
            a,b=list[0],list[1]
            size=min(a[1],b[1])
            if size==0:
                if a[1]==0:
                    break
                elif a[1]==1:
                    r+=a[0]
                else:
                    return ''
            r+=(a[0]+b[0])*size
            list[0][1]-=size
            # if list[0][1]>0:
            #     r+=a[0]
            #     list[0][1]-=1
            list[1][1]=0

        return r
s=Solution()
test=[
{"input":"aaab", "output":""},
{"input":"abbabbaaab", "output":"ababababab"},
{"input":"bbbbbb", "output":""},
{"input":"vvvlo", "output":"vlvov"},
{"input":"aab", "output":"aba"},

]

for t in test:
    r=s.reorganizeString(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))


