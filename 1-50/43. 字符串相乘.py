class Solution:

    def add(self,index,result,ans):
        if index>= len(result):
            result.append(ans)
        else:
            temp = result[index] + ans
            if temp >= 10:
                self.add(index+1,result,1)
                temp = temp - 10
            result[index] = temp

    def multiply(self, num1, num2):
        list1,list2=self.strToList(num1),self.strToList(num2)
        list1.reverse()
        list2.reverse()
        len1,len2=len(list1),len(list2)
        result=[]
        k=0
        l=0
        for j in range(len2):
            for i in range(len1):
                ans=list1[i]*list2[j]+k
                if ans>=10:
                    k=int(ans/10)
                    ans=ans-k*10
                else:
                    k=0
                self.add(i+j,result,ans)
            if k!=0:
                self.add(i+j+1, result,k )
                k=0

        if k != 0:
            self.add(len1+len2+1, result,k)
            k=0
        result.reverse()
        s=''
        l=True
        for r in result:
            if r==0 and l:
                continue
            else:
                l=False
            s+=str(r)
        if ""==s:
            return "0"
        return s

    def strToList(self,num):
        list = []
        for n in num:
            list.append(int(n))
        return list


s=Solution()

test=[
{"input":["91515","0"],"output":"0"},
{"input":["9","9"],"output":"81"},
{"input":["123","456"],"output":"56088"},
{"input":["2","3"],"output":"6"},

      ]

for t in test:
    r=s.multiply(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.multiply(t['input'][0],t['input'][1])