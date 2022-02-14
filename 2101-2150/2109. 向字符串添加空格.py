class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        size=len(spaces)
        spaces.insert(0,0)
        spaces.append(len(s))
        ans=''
        for i in range(size+1):
            ans+=s[spaces[i]:spaces[i+1]]+' '

        return ans[:-1]