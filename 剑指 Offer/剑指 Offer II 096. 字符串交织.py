class Solution:
    def isInterleave(self, s1, s2, s3):
        l1,l2,l3=0,0,0
        size1,size2,size3=len(s1),len(s2),len(s3)
        if size1+size2!=size3:
            return False
        dp=[ [0 for i in range(size2+1)] for j in range(size1+1)]
        dp[0][0]=1
        for i in range(1,size1+1):
            if s1[i-1]==s3[i-1]:
                dp[i][0]=1
            else:
                break
        for i in range(1,size2+1):
            if s2[i-1]==s3[i-1]:
                dp[0][i]=1
            else:
                break
        for i in range(1,size1+1):
            for j in range(1,size2+1):
                k=i+j-1
                if dp[i-1][j]==1 and s1[i-1]==s3[k]:
                    dp[i][j]=1
                if dp[i][j-1]==1 and s2[j-1]==s3[k]:
                    dp[i][j]=1
        if dp[size1][size2]==1:
            return True
        else:
            return False