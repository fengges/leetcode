class Solution:
    def findRedundantConnection(self, edges):
        r=None
        start = 0
        graphs = {}
        dict = {}
        for line in edges:
            index0 = dict.get(line[0], None)
            index1 = dict.get(line[1], None)

            if index0 is None and index1 is None:
                tmp = set()
                tmp.add(line[0])
                tmp.add(line[1])
                dict[line[0]] = start
                dict[line[1]] = start
                graphs[start] = tmp
                start += 1
            elif index0 == index1:
                r = line
                continue
            elif index0 is not None and index1 is not None:

                index0, index1 = min(index0, index1), max(index0, index1)
                graph = graphs.pop(index1)
                for g in graph:
                    graphs[index0].add(g)
                    dict[g] = index0
            elif index0 is not None:
                dict[line[1]] = index0
                graphs[index0].add(line[1])
            elif index1 is not None:
                dict[line[0]] = index1
                graphs[index1].add(line[0])
        return r

s=Solution()

test=[
{"input":[[1,2],[1,3],[2,3]],"output":[2,3]},

]
for t in test:
    r=s.findRedundantConnection(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
