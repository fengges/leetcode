class Solution:
    def repeatedNTimes(self, A):
        dic={}
        for a in A:
            if a in dic:
                return a
            dic[a]=1
        