class Solution:
    def lexicalOrder(self, n):
        tmp=list(map(str,range(1,n+1)))
        tmp.sort()
        return tmp