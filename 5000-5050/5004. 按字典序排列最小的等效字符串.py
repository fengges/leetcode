class Solution:
    def smallestEquivalentString(self, A, B, S):
        size=len(A)
        data=[]
        for i in range(size):
            data.append([A[i],B[i]])
        start = 0
        graphs = {}
        dict = {}
        for line in data:
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

        for g in graphs:
            graphs[g]=list(graphs[g])
            graphs[g].sort()
        r=""
        for s in S:
            if s in dict:
                r+=graphs[dict[s]][0]
            else:
                r+=s
        return r