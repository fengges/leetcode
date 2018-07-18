class Solution(object):
    def numJewelsInStones(self, J, S):
        num=0
        for j in J:
            for s in S:
                if j==s:
                    num+=1
        return num