class Solution:
    def longestSubstring(self, s, k):
        return self.longestSubstring2(s, k, 0,len(s)-1)
    def longestSubstring2(self, s, k,left ,right):
        if left > right:
            return 0
        dict={}
        for i in range(left,right+1):
            dict[s[i]]=dict.get(s[i],0)+1

        while left <= right and dict[s[left]] < k:
            dict[s[left]] -= 1
            left += 1

        while left <= right and dict[s[right]] < k:
            dict[s[right]] -= 1
            right -= 1

        for index in range(left+1,right):
            if dict[s[index]] < k:
                return max(self.longestSubstring2(s, k, left, index - 1),self.longestSubstring2(s, k, index + 1, right))
        return right - left + 1

s=Solution()
test=[
{"input":["ababacb",3] , "output":0},
]
for t in test:
    r=s.longestSubstring(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))