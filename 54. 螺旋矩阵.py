class Solution:
    def spiralOrder(self, matrix):
        size = len(matrix)
        if size == 0:
            return []
        length = len(matrix[0])
        l, r = 0, length
        t, b = 0, size
        result = []
        flag=True
        while l<r:

            if flag:
                flag=False
            else:
                break
            for i in range(l, r):
                flag=True
                result.append(matrix[t][i])
            t += 1

            if flag:
                flag=False
            else:
                break
            for i in range(t, b):
                flag = True
                result.append(matrix[i][r - 1])
            r -= 1

            if flag:
                flag=False
            else:
                break
            for i in range(r - 1, l - 1, -1):
                flag = True
                result.append(matrix[b - 1][i])
            b -= 1

            if flag:
                flag=False
            else:
                break
            for i in range(b - 1, t - 1, -1):
                flag = True
                result.append(matrix[i][l])
            l += 1

        return result


s = Solution()

test = [
    {"input": [[2,5,8],[4,0,-1]], "output": [2,5,8,-1,0,4]
     },
    {"input":[[6,9,7]], "output":[6,9,7]
    },
    {"input":[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
], "output":[1,2,3,4,8,12,11,10,9,5,6,7]
    },
    {"input": [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
], "output": [1,2,3,6,9,8,7,4,5]
    },

]

for t in test:
    r = s.spiralOrder(t['input'])
    if r != t['output']:
        print("error:" + str(t) + " out:" + str(r))
        r = s.spiralOrder(t['input'])

