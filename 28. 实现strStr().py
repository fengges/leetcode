class Solution:
    def strStr(self, haystack, needle):
        i=0
        j=0
        if len(needle)==0:
            return 0
        while i<len(haystack)-len(needle) and j<len(needle):
            h=i
            n=j
            while h<len(haystack) and n<len(needle) and needle[n]==haystack[h]:
                h+=1
                n+=1
            if n==len(needle):
                return i
            else:
                i+=1
                j=0
        return -1


s=Solution()

test=[
{"input": ["hello","ll"],"output":2},
{"input":["aaaaa","bba"],"output":-1},
      ]

for t in test:
    r=s.strStr(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.strStr(t['input'][0],t['input'][1])

