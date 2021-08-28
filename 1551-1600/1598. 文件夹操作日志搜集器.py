class Solution:
    def minOperations(self, logs) -> int:
        ans=0
        for l in logs:
            if l.startswith('..'):
                ans-=1
                ans=max(0,ans)
            elif l.startswith('.'):
                pass
            else:
                ans+=1
        return ans