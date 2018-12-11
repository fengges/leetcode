class Solution:
    def palindromePairs(self, words):
        dic={w:i for i,w in enumerate(words)}
        r=[]
        for word in words:
            tmp=word[::-1]
            if word==tmp:
                continue
            if tmp in dic:
                r.append([dic[tmp],dic[word]])
        return r


