import functools
def cmp(a,b):
    if a[1]==b[1]:
        return 1 if a[0]>b[0] else -1
    else:
        return 1 if a[1]>b[1] else -1
class Solution:
    def reorderLogFiles(self, logs):
        list1=[]
        list2=[]
        for log in logs:
            flag,id,cont=self.judge(log)
            if not flag:
                list1.append([id,cont])
            else:
                list2.append(id+" "+cont)
        list1.sort(key=functools.cmp_to_key(cmp))
        r=[i[0]+" "+i[1]  for i in list1]
        r.extend(list2)
        return r
    def judge(self,log):
        tmp=log.split(' ')
        flag=True
        for t in range(1,len(tmp)):
            if not tmp[t].isdigit():
                flag=False
        return flag,tmp[0]," ".join(tmp[1:])
s=Solution()
test=[
{"input":["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"], "output":["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]},
]
for t in test:
    r=s.reorderLogFiles(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
