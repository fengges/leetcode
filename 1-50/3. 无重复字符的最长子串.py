class Solution:
    def lengthOfLongestSubstring(self, s):
        maxL=0
        l=0
        dic=[]
        for i in s:
            if i not in dic:
                l+=1
                dic.append(i)
                if l>maxL:
                    maxL=l
            else:
                index=dic.index(i)
                dic=dic[index+1:]
                dic.append(i)
                l=len(dic)
        return maxL

s=Solution()

test=[{"input":"babad","output":3},
        {"input":"bbbbb","output":1},
        {"input":"pwwkew","output":3},
        {"input":"abb","output":2},
        {"input":"dvdf","output":3},
      ]

for t in test:
    r=s.lengthOfLongestSubstring(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.lengthOfLongestSubstring(t['input'])



