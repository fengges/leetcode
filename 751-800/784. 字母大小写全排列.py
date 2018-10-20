class Solution:
    def letterCasePermutation(self, S):
        tmp=[i for i in S]
        r=[]
        self.find(0,tmp,r)
        return r
    def find(self,start,tmp,r):
        if start==len(tmp):
            r.append(''.join(tmp))
        elif tmp[start].isdigit():
            self.find(start+1,tmp,r)
        else:
            tmp[start]=tmp[start].lower()
            self.find(start+1,tmp,r)
            tmp[start] = tmp[start].upper()
            self.find(start + 1, tmp, r)

