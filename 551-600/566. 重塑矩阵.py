class Solution:
    def matrixReshape(self, nums, r, c):
        if r*c!=len(nums)*len(nums[0]):
            return nums
        result=[[0 for j in range(c)] for i in range(r)]
        for i,value in enumerate(nums):
            for j ,v in enumerate(value):
                index=(i)*len(nums[0])+j
                x=int(index/c)
                y=index-x*c
                result[x][y]=nums[i][j]
        return result

s = Solution()
test = [
{"input": [[[1,2],
 [3,4]],1,4], "output": [[1,2,3,4]]},
{"input": [[[1,2],
 [3,4]],2,4], "output": [[1,2],
 [3,4]]},

]

for t in test:
    r = s.matrixReshape(t['input'][0],t['input'][1],t['input'][2])
    if r != t['output']:
        print("error:" + str(t) + " out:" + str(r))
        r = s.matrixReshape(t['input'][0], t['input'][1],t['input'][2])
