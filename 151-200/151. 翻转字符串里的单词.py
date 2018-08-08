class Solution(object):
    def reverseWords(self, s):
        words=s.split(" ").reverse()
        result=[w for w in words if len(w)>0]
        return result


