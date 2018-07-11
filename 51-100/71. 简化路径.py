class Solution:
    def simplifyPath(self, path):
        list=path.split("/")
        list.reverse()
        father=0
        result=[]
        for l in list:
            if len(l)==0:
                continue
            if l=="..":
                father+=1
            elif l=='.':
                continue
            else:
                if father>0:
                    father-=1
                    continue
                else:
                    result.append(l)
        result.reverse()
        s="/"+"/".join(result)
        return s



s=Solution()

test=[
{"input":"/home/","output":"/home"},

]
for t in test:
    r=s.simplifyPath(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.simplifyPath(t['input'])