class Solution:
    def readBinaryWatch(self, num):
        r=[]
        for i in range(12):
            for j in range(60):
                if self.get(i)+self.get(j)==num:
                    if j<10:
                        r.append(str(i)+":0"+str(j))
                    else:
                        r.append(str(i) + ":"+str(j))
        return r

    def get(self,num):
        r=0
        while num!=0:
            if num%2==1:
                r+=1
            num//=2
        return r