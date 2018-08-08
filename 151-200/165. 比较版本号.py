class Solution:
    def compareVersion(self, version1, version2):
        v1=version1.split(".")
        v2 = version2.split(".")
        while len(v1)>0 and int(v1[-1])==0:
            del v1[-1]
        while len(v2)>0 and int(v2[-1])==0:
            del v2[-1]
        i=0
        while i<min(len(v1),len(v2)):
            tmp=int(v1[i])-int(v2[i])
            if tmp==0:
                i+=1
            elif tmp>0:
                return 1
            else:
                return -1
        if len(v1)==len(v2):
            return 0
        elif len(v1)>len(v2):
            return 1
        else:
            return -1

s=Solution()
test=[
{"input":["1","0"], "output":-1},
{"input":["0.1","1.1"], "output":-1},
]

for t in test:
    r=s.compareVersion(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.compareVersion(t['input'][0], t['input'][1])