class Solution:
    def exist(self, board, word):
        if len(word)==0:
            return False
        list=self.find(board,word[0])
        for l in list:
            mark = [[True for t in temp] for temp in board]
            r=self.search(board, word, mark,l[0],l[1])
            if r==True:
                return True
        return False
    def search(self,borad,word,mark,i,j):
        if len(word)==0:
            return True
        if i<0 or i>=len(borad) or j<0 or j>=len(borad[0]):
            return False
        if mark[i][j] and borad[i][j]==word[0]:
            mark[i][j]=False
            falg=self.search(borad,word[1:],mark,i+1,j) or self.search(borad,word[1:], mark, i - 1, j) or  self.search(borad,word[1:], mark, i , j+1) or self.search(borad,word[1:], mark, i , j-1)

            mark[i][j] = True
            return falg
        else:
            return False

    def find(self,board,s):
        list=[]
        for i,temp in enumerate(board):
            for j,t in enumerate(temp):
                if t==s:
                    list.append([i,j])
        return list

s=Solution()

test=[
    {"input":[[["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]],"ABCESEEEFS"],"output":True},
    {"input":[[["C","A","A"],["A","A","A"],["B","C","D"]],"AAB"],"output":True},
    {"input":[[
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ],"ABCCED"],"output":True},
    {"input":[[
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ],"SEE"],"output":True},
    {"input":[[
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ],"ABCB"],"output":False},

]
for t in test:
    r=s.exist(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.exist(t['input'][0], t['input'][1])