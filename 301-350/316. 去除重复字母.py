class Solution:
    def removeDuplicateLetters(self, s):
        vec=[0 for i in range(256)]
        visited=[False for i in range(256)]
        for c in s:
            vec[ord(c)]+=1
        res = ""
        for  c in  s:
            vec[ord(c)] -=1
            if visited[ord(c)]:
                continue
            while len(res)>0 and vec[ord(res[-1])] and c < res[-1]:
                visited[ord(res[-1])] = False
                res=res[:-1]
            res += c
            visited[ord(c)] =True
        return res
