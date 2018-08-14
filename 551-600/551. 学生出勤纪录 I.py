class Solution:
    def checkRecord(self, s):
        n=0
        index=s.find("LLL")
        if index>=0:
            return False
        for i in s:
            if 'A'==i:
                n+=1
        if n>1:
            return False
        return True