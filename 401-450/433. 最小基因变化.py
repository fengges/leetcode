class Solution(object):
    def minMutation(self, start, end, bank):
        if end not in bank:
            return -1
        if start not in bank:
            bank.insert(0,start)
        head=[[] for i in bank]
        dic={v:i for i,v in enumerate(bank)}
        flag=[True for i in bank]
        alf="ACGT"
        for word in bank:
            for i in range(len(word)):
                tmp_s=word[0:i]
                tmp_e=word[i+1:]
                for j in alf:
                    tmp_w=tmp_s+j+tmp_e
                    if tmp_w in dic:
                        head[dic[word]].append(dic[tmp_w])
        start = dic[start]
        end=dic[end]
        length=[0 for i in bank]
        length[start]=1
        flag[start]=False
        vector=[start]
        while len(vector)!=0:
            start=vector[0]
            words=head[start]
            for w in words:
                if flag[w]:
                    length[w]=length[start]+1
                    flag[w]=False
                    vector.append(w)
            del vector[0]
        return length[end]