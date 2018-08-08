import re
class Solution:
    def mostCommonWord(self, paragraph, banned):
        rr = re.compile(r'[a-zA-Z]+')
        words=rr.findall(paragraph.lower())
        dic={}
        for i in words:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        maxKey=None
        for k in dic:
            if (maxKey is None or dic[k]>dic[maxKey]) and k not in banned:
                maxKey=k
        return maxKey
    def mostCommonWord2(self, paragraph, banned):
        words=paragraph.split(' ')
        dic={}
        for w in words:
            w=self.replace(w).lower()
            if w not in dic:
                dic[w]=0
            dic[w]+=1
        maxKey=None
        for k in dic:
            if (maxKey is None or dic[k]>dic[maxKey]) and k not in banned:
                maxKey=k
        return maxKey
    def replace(self,s):
        re="!?',;."
        for r in re:
            s=s.replace(r,'',len(s))
        return s
s = Solution()
test = [
    {"input":["Bob hit a ball, the hit BALL flew far after it was hit.",["hit"]], "output":"ball"},

]

for t in test:
    r = s.mostCommonWord(t['input'][0],t['input'][1])
    if r != t['output']:
        print("error:" + str(t) + " out:" + str(r))
        r = s.mostCommonWord(t['input'][0], t['input'][1])