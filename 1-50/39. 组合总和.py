import copy
class Solution:
    def count(self,candidates,target,result):
        if target==0:
            self.result.append(copy.deepcopy(result))
        elif target>0 and len(candidates)>0:
            #不要当前元素
            self.count(candidates[1:],target,result)
            # 要当前元素
            result.append(candidates[0])
            self.count(candidates, target-candidates[0],result)
            result.pop()

    def combinationSum(self, candidates, target):
        self.result = []
        self.count(candidates,target,[])
        return self.result

s=Solution()

test=[
{"input":[[3,33,333],10000],"output":[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]},
{"input":[[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25],10],"output":[
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
    r=s.combinationSum(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
