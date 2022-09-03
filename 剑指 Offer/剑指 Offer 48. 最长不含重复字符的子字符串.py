class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=0
        t=''
        for a in s:
            if a in t:
                t=t[t.index(a)+1:]+a
                # print(a,t)
            else:
                t+=a
            ans=max(ans,len(t))
        return ans