class Solution:
    def kWeakestRows(self, mat, k) :
        ans=[[i,sum(m)] for i,m in enumerate(mat)]
        ans=sorted(ans,key=lambda x:x[1])
        return [a[0] for a in ans[:k]]