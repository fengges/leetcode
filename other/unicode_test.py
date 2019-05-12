class test:
    def __init__(self):
        self.list = [[float("-inf"), float("-inf"),-1], [float("inf"), float("inf"), -1]]
    def add(self, start, end):
        i = 0
        while i < len(self.list) - 1 and start < end:
            if self.list[i][1] <= start and self.list[i + 1][0] >= end:
                self.list.insert(i + 1, [start, end, 1])
                break

            elif not (self.list[i][1] <= start or end <= self.list[i][0]):
                t = [self.list[i][0], self.list[i][1], start, end]
                t.sort()
                tmp = self.list.pop(i)
                if t[0] != t[1]:
                    num = tmp[2]
                    if t[0] == start:
                        num = 1
                    self.list.insert(i, [t[0], t[1], num])
                    i += 1
                self.list.insert(i, [t[1], t[2], tmp[2] + 1])
                start = t[2]
                if start == end and start != t[3]:
                    self.list.insert(i + 1, [start, t[3], tmp[2]])
                    break
            else:
                i += 1
    def get(self, k):
        r = []
        for line in self.list:
            if line[-1] >= k:
                if len(r)>0 and line[0]==r[-1][1]:
                    r[-1][-1]=line[1]
                else:
                    r.append([line[0], line[1]])
        return r


t = test()
A = input().split(' ')
N, K = int(A[0]), int(A[1])
for k in range(N):
    B = input().split(' ')
    # int(B[0]), int(B[1])
    t.add(int(B[0]), int(B[1]))
r = t.get(K)
print(len(r))

for tmp in r:
    print(tmp[0], tmp[1])

