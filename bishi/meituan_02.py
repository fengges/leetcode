def indegree0(v, e):
    if v == []:
        return None
    tmp = v[:]
    for i in e:
        if i[1] in tmp:
            tmp.remove(i[1])
    if tmp == []:
        return -1

    for t in tmp:
        for i in range(len(e)):
            if t in e[i]:
                e[i] = 'toDel'  # 占位，之后删掉
    if e:
        eset = set(e)
        eset.remove('toDel')
        e[:] = list(eset)
    if v:
        for t in tmp:
            v.remove(t)
    return tmp
def topoSort(v, e):
    result = []
    while True:
        nodes = indegree0(v, e)
        if nodes == None:
            break
        if nodes == -1:
            return None
        result.extend(nodes)
    return result
import sys
line= sys.stdin.readline().strip()
node=list(set(line.replace(" ","")[::]))
egde=[]
words=line.split(" ")
for i in range(len(words)-1):
    word1=words[i]
    word2 = words[i+1]
    size=min(len(word1),len(word2))
    for i in range(size):
        if word1[i]!=word2[i]:
            egde.append((word1[i],word2[i]))
            break

r=topoSort(node,egde)

print(r)