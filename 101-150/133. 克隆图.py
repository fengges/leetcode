class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None
        dic={}
        dic[node.label] = [i.label for i in node.neighbors]
        head=node.label
        self.getDic(node.neighbors,dic)
        nodes=[UndirectedGraphNode(k) for k in dic]
        new_dic={v.label:i for i,v in enumerate(nodes)}
        for n in nodes:
            neighbors=dic[n.label]
            node=nodes[new_dic[n.label]]
            for tmp in neighbors:
                node.neighbors.append(nodes[new_dic[tmp]])
        return nodes[new_dic[head]]
    def getDic(self,nodes,dic):
        for n in nodes:
            if n.label in dic:
                continue
            else:
                dic[n.label]=[i.label for i in n.neighbors]
                self.getDic(n.neighbors,dic)
a=UndirectedGraphNode(-1)
b=UndirectedGraphNode(1)
a.neighbors.append(b)
s=Solution()
test=[
{"input": a, "output":"IPv4"},
]

for t in test:
    r=s.cloneGraph(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))

