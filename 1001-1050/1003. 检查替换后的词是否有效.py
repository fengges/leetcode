class Solution:
    def isValid(self, S):
        tmp=[0,0,0]
        for s in S:
            if s=="a":
                tmp[0]+=1
            elif s=='b':
                tmp[1]+=1
                if tmp[0]<tmp[1]:
                    return False
            else:
                tmp[2]+=1
                if tmp[0]<tmp[2] or tmp[1]<tmp[2]:
                    return False
        return True
