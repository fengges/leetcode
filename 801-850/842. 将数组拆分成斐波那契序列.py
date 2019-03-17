class Solution:
    def splitIntoFibonacci(self, S):
        num=S
        res = [[int(num[0])]]
        for n in range(1, len(num)):
            i = num[n]
            t = int(i)
            res.append([res[-1][0] * 10 + t])
            size = len(res) - 1
            j = 0
            while j < size:
                r = res[j]
                if len(r) == 1:
                    r.append(t)
                elif len(r) == 2:
                    if self.judge(r[0], r[1], t):
                        r.append(t)
                        res.insert(len(res)-1,[r[0], r[1] * 10 + t])
                    else:
                        r[1] = r[1] * 10 + t
                else:
                    if r[-1] == r[-2] + r[-3]:
                        if self.judge(r[-1], r[-2], t):
                            r.append(t)
                        else:
                            res.pop(j)
                            j -= 1
                            size -= 1
                    else:
                        r[-1] = r[-1] * 10 + t
                        if not self.judge(r[-3], r[-2], r[-1]):
                            res.pop(j)
                            j -= 1
                            size -= 1
                j += 1
        tmp = [r for r in res if len(r) >= 3 and r[-3] + r[-2] == r[-1] and "".join([str(a) for a in r]) == num and max(r)<=2**31-1]
        return tmp[0] if len(tmp)>0 else []

    def judge(self, r1, r2, t):
        return str(r1 + r2).startswith(str(t))

s=Solution()

test=[
{"input":"539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511","output": True},
{"input":"65155860565120123725188845312570501415813985131540021293853444785557417090189551459312523612080","output": True},
{"input":"112358130","output": True},

]
for t in test:
    r=s.splitIntoFibonacci(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))