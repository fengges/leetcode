class Solution:
    def findSubstring(self, s, words):
        result=[]
        for w in words:
            index=s.find(w)
            if index<0:
                return []
            else:
                result.append(index)
        result.sort()
        size=len(words[0])
        for i in range(1,len(result)):
            if result[i]-result[i-1]!=size:
                return []
