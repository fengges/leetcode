import copy
class Solution:
    def allPathsSourceTarget(self, graph):
        self.r=[]
        flag=[True for i in  graph]
        flag[0]=False
        self.find(graph,flag,[0])
        return self.r
    def find(self,graph,flag,path):
        t=graph[path[-1]]
        for i in t:
            if i==len(flag)-1:
                tmp=copy.deepcopy(path)
                tmp.append(i)
                self.r.append(tmp)
            elif flag[i]:
                flag[i]=False
                path.append(i)
                self.find(graph,flag,path)
                flag[i]=True
                del path[-1]
s=Solution()
test=[
{"input":[[1,2], [3], [3], []] , "output": [[0,1,3],[0,2,3]] },

]

for t in test:
    r=s.allPathsSourceTarget(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
