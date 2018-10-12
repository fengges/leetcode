class Solution:
    def checkInclusion(self, s1, s2):
        tmp = {}
        p=s1
        s=s2
        size = len(p)
        if len(s) < size:
            return False
        for i in p:
            if i not in tmp:
                tmp[i] = 0
            tmp[i] += 1

        dic = {i: 0 for i in s}
        for i in range(size):
            dic[s[i]] += 1
        r = []
        for i in range(len(s) - size + 1):
            if self.judge(dic, tmp):
                r.append(i)
            if i == len(s) - size:
                break
            dic[s[i]] -= 1
            dic[s[i + size]] += 1
        return len(r)!=0

    def judge(self, dic, tmp):
        for k in dic:
            if k not in tmp and dic[k] > 0:
                return False
            elif k in tmp and dic[k] != tmp[k]:
                return False
        return True