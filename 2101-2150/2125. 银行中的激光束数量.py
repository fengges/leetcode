class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans=[[c for c in b if c=='1'] for b in bank]
        ans=[len(a) for a in ans if a]
        r=0
        for i in range(len(ans)-1):
            r+=ans[i]*ans[i+1]
        return r
