class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        size1,size2=len(s1),len(s2)
        if size1!=size2:
            return False
        ans=[[s1[i],s2[i]]  for i in range(size1) if s1[i]!=s2[i]]
        return True if len(ans)==0 or (len(ans)==2 and ans[0][0]==ans[1][1] and ans[1][0]==ans[0][1]) else False