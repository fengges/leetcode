class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs)==0:
            return ''
        temp=strs[0]
        t=''
        for i in range(1,len(temp)+1):
            t=temp[0:i]
            for s in strs:
                if s.find(t)!=0:
                    return t[0:-1]
        if t==temp:
            return temp
        return ''
s=Solution()

test=[

{"input": ["a"],"output":"a"},
{"input": [""],"output":""},
{"input": ["flower","flow","flight"],"output":"fl"},
{"input":["dog","racecar","car"],"output":''},

      ]

for t in test:
    r=s.longestCommonPrefix(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.longestCommonPrefix(t['input'])