class Solution:
    def minDistance(self, word1, word2):
        result=[[0 for i in range(len(word2)+1)] for j in range(len(word1)+1)]
        for i in range(len(result)):
            result[i][0]=i
        for j in range(len(result[0])):
            result[0][j]=j
        for i,w1 in enumerate(word1):
            for j,w2 in enumerate(word2):
                if w1==w2:
                    rep=result[i][j]
                else:
                    rep = result[i][j]+1
                ins_del = min(result[i+1][j], result[i][j+1]) + 1
                result[i+1][j+1] = min(rep, ins_del)

        return result[-1][-1]