class Solution:
    def buddyStrings(self, A, B):
        if len(A)!=len(B):
            return False
        diff=[]
        for i in range(len(A)):
            if A[i]!=B[i]:
                diff.append(i)
        if len(diff)==0:
            dic={}
            for i in A:
                if i not in dic:
                    dic[i]=0
                dic[i]+=1
            t=[0 for k in dic if dic[k]>1]
            return len(t)>0
        elif len(diff)==2:
            return A[diff[0]]==B[diff[1]] and A[diff[1]]==B[diff[0]]
        else:
            return False

s=Solution()
test=[
{"input":["aa","aa"], "output":True},

]
for t in test:
    r=s.buddyStrings(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
