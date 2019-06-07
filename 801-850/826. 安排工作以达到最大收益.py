class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        pair = [[difficulty[i], profit[i]] for i in range(len(difficulty))]
        pair.sort()
        worker.sort()
        tmp, res, loc = 0, 0, 0

        for man in worker:
            while loc < len(difficulty) and man >= pair[loc][0]:
                tmp = max(tmp, pair[loc][1])
                loc += 1
            res += tmp
            print(man,tmp)
        return res
s=Solution()
test=[
{"input":[[23,30,35,35,43,46,47,81,83,98],[8,11,11,20,33,37,60,72,87,95],[95,46,47,97,11,35,99,56,41,92]],"output":553},
]
for t in test:
    r=s.maxProfitAssignment(t['input'][0],t['input'][1],t['input'][2])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        # r = s.reverseBetween(t['input'][0], t['input'][1], t['input'][2])