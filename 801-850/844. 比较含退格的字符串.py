class Solution:
    def backspaceCompare(self, S, T):
        return self.stack(S)==self.stack(T)
    def stack(self,str):
        r=[]
        for s in str:
            if s=="#":
                if len(r)>0:
                    del r[-1]
            else:
                r.append(s)
        return ''.join(r)

