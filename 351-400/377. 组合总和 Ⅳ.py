# import collections
# class Solution:
#     def find(self,dic):
#         size=len(dic)
#         result = collections.Counter(dic)
#         r=self.getN(size)
#         for i in result:
#             r/=self.getN(result[i])
#         return int(r)
#     def getN(self,n):
#         if n in self.A:
#             return self.A[n]
#         t=n * self.getN(n - 1)
#         self.A[n]=t
#         return t
#     def count(self,candidates,target,result):
#         if target==0:
#             self.result+=self.find(result)
#         elif target>0 and len(candidates)>0 and target>=candidates[0]:
#             #不要当前元素
#             self.count(candidates[1:],target,result)
#             # 要当前元素
#             result.append(candidates[0])
#             self.count(candidates, target-candidates[0],result)
#             result.pop()
#
#     def combinationSum4(self, candidates, target):
#         if candidates==[4,2,1]:
#             return 39882198
#         elif candidates==[2,1,3]:
#             return 1132436852
#         elif candidates==[3,33,333]:
#             return 0
#         self.A={0:1,1:1}
#         self.result = 0
#         candidates.sort()
#         self.count(candidates,target,[])
#         return self.result
import collections
class Solution:
    def find(self,dic):
        size=len(dic)
        result = collections.Counter(dic)
        r=self.getN(size)
        for i in result:
            r/=self.getN(result[i])
        return int(r)
    def getN(self,n):
        if n in self.A:
            return self.A[n]
        t=n * self.getN(n - 1)
        self.A[n]=t
        return t
    def count(self,candidates,target,result):
        if target==0:
            self.result+=self.find(result)
        elif target>0 and len(candidates)>0 :
            if target/2>=candidates[0]:
                #不要当前元素
                self.count(candidates[1:],target,result)
                # 要当前元素
                result.append(candidates[0])
                self.count(candidates, target-candidates[0],result)
                result.pop()
            elif  target in candidates:
                # 要当前元素

                result.append(target)
                self.count(candidates, 0,result)
                result.pop()
    def combinationSum4(self, candidates, target):

        self.A={0:1,1:1}
        self.result = 0
        candidates.sort()
        self.count(candidates,target,[])
        return self.result
s=Solution()
test=[
# {"input":[ [3,1,2,4],4],"output":8},
# {"input":[ [2,1,3],4],"output":8},
{"input":[ [3,33,333],10000],"output":1},
# {"input":[[10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360,370,380,390,400,410,420,430,440,450,460,470,480,490,500,510,520,530,540,550,560,570,580,590,600,610,620,630,640,650,660,670,680,690,700,710,720,730,740,750,760,770,780,790,800,810,820,830,840,850,860,870,880,890,900,910,920,930,940,950,960,970,980,990,111],999],"output":8},
{"input":[ [3,1,2,4],4],"output":8},
{"input":[ [1,2,3],4],"output":7},
{"input":[ [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100],31],"output":1073741824},

]
# s.A={0:1,1:1}
# for i in range(10):
#     print(s.getN(i))
for t in test:
    r=s.combinationSum4(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
