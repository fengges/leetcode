class Solution:
    def minWindow(self, s, t):

        srcHash = [0 for i in range(256)]
        for t1 in t:
            srcHash[ord(t1)]+=1
        start = 0
        destHash = [0 for i in range(256)]
        found = 0
        begin = -1
        end =len(s)
        minLength = end
        for i in range(len(s)):
            destHash[ord(s[i])]+=1
            if destHash[ord(s[i])] <= srcHash[ord(s[i])]:
                found+=1
            if found == len(t):
                while start < i and destHash[ord(s[start])] > srcHash[ord(s[start])]:
                    destHash[ord(s[start])]-=1
                    start+=1
                if i - start < minLength:
                    minLength = i - start
                    begin = start
                    end = i
                destHash[ord(s[start])]-=1
                found-=1
                start+=1
        if begin==-1:
            return ""
        return  s[begin:end+1]

s=Solution()

test=[
{"input":["ab","a"],"output":"a"},
{"input":["ADOBECODEBANC","ABC"],"output":"BANC"},


]
for t in test:
    r=s.minWindow(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.minWindow(t['input'][0], t['input'][1])