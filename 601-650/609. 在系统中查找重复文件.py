class Solution:
    def findDuplicate(self, paths):
        dic={}
        for p in paths:
            path=p.split(" ")
            root=path[0]
            file=path[1:]
            for f in file:
                name,content=self.getName(f)
                if content in dic:
                    dic[content].append(root+'/'+name)
                else:
                    dic[content]=[root+'/'+name]
        result=[]
        for k in dic:
            if len(dic[k])>1:
                result.append(dic[k])
        return result
    def getName(self,f):
        index=f.find("(")
        name=f[0:index]
        content=f[index+1:-1]
        return name,content

