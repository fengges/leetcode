class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ans=""
        st=0
        for a in s:
            if a=='(':
                ans+=a
                st+=1
            elif a==')':
                if st==0:
                    continue
                else:
                    st-=1
                    ans+1