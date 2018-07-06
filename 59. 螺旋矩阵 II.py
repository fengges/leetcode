class Solution:
    def generateMatrix(self, n):
        size ,length =n,n
        l, r = 0, length
        t, b = 0, size
        result = [[0 for j in range(n)] for i in range(n)]
        flag=True
        temp=1
        while l<r:

            if flag:
                flag=False
            else:
                break
            for i in range(l, r):
                flag=True
                result[t][i]=temp
                temp+=1
            t += 1

            if flag:
                flag=False
            else:
                break
            for i in range(t, b):
                flag = True
                result[i][r - 1]=temp
                temp+=1
            r -= 1

            if flag:
                flag=False
            else:
                break
            for i in range(r - 1, l - 1, -1):
                flag = True
                result[b - 1][i]=temp
                temp+=1
            b -= 1

            if flag:
                flag=False
            else:
                break
            for i in range(b - 1, t - 1, -1):
                flag = True
                result[i][l]=temp
                temp+=1
            l += 1

        return result


s = Solution()

test = [
    {"input": 3, "output": [
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
     },
]

for t in test:
    r = s.generateMatrix(t['input'])
    if r != t['output']:
        print("error:" + str(t) + " out:" + str(r))
        r = s.generateMatrix(t['input'])

