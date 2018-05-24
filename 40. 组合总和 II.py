import copy
class Solution:
    def count(self,candidates,target,result):
        if target==0:
            s=str(result)
            if s not in self.dic:
                self.dic[s]=" "
                self.result.append(copy.deepcopy(result))
        elif target>0 and len(candidates)>0:
            #不要当前元素
            self.count(candidates[1:],target,result)
            # 要当前元素
            result.append(candidates[0])
            self.count(candidates[1:], target-candidates[0],result)
            del result[-1]

    def combinationSum2(self, candidates, target):
        candidates.sort()
        self.dic={}
        self.result=[]
        self.count(candidates,target,[])
        return self.result


s=Solution()

test=[
{"input":[[14,18,19,30,6,5,14,23,28,18,26,21,12,15,29,18,32,23,6,21,19,30,6,28,17,13,29,28,10,34,26,11,10,32,7,11,32,8,21,18,22,5,34,21,7,20,26,5,9,28,21,23,23,15,8,27,23,32,12,20,31,33,27,28,30,21,34,19]
,29],"output":[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]},
{"input":[ [10,1,2,7,6,1,5],8],"output":[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]},
{"input":[ [2,5,2,1,2],5],"output":[
  [1,2,2],
  [5]
]},
 ]

for t in test:
    r=s.combinationSum2(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.combinationSum2(t['input'][0],t['input'][1])
