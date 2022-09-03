class Solution:
    def printVertically(self, s: str) -> List[str]:
        words=s.split(' ')
        maxl=max([len(w) for w in words])
        tmp=[' '*(maxl-len(w))+w  for w in words]
        ans=[]
        for i in range(maxl):
            ans.append([t[i] for t in tmp])
        return ans