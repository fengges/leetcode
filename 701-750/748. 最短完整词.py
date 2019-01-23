class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        licensePlate=licensePlate.lower()
        dic={}
        for l in licensePlate:
            if ord(l)<ord('a') or ord(l)>ord('z'):
                continue
            if l not in dic:
                dic[l]=0
            dic[l]+=1
        r=None
        for w in words:
            w=w.lower()
            tmp=self.getdic(w)
            if self.compare(dic,tmp):
                if r is None or len(w)<len(r):
                    r=w
        return r
    def compare(self,A,B):
        for k in A:
            if k not in B or B[k]<A[k]:
                return False
        return True
    def getdic(self,w):
        dic={}
        for l in w:
            if l not in dic:
                dic[l]=0
            dic[l]+=1
        return dic
