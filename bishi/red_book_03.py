import sys
N=int(sys.stdin.readline().strip())
line = sys.stdin.readline().strip()
values = list(map(int, line.split()))


def func(values,N):
    dp = [[0, 0] for i in range(N + 1)]

    for i in range(1, N + 1):
        dp[i][0] += max(dp[i - 1])
        dp[i][1] += dp[i - 1][0] + values[i - 1]
    maxn = max(dp[-1])

    def deep(dp, last, index):
        if index == 0:
            return 0
        if last == True:
            return deep(dp, False, index - 1)
        else:
            if dp[index][0] > dp[index][1]:
                return deep(dp, False, index - 1)
            elif dp[index][0] < dp[index][1]:
                return deep(dp, True, index - 1) + 1
            else:
                return min(deep(dp, True, index - 1) + 1, deep(dp, False, index - 1))
    return maxn, min(deep(dp, True, N - 1) + 1, deep(dp, False, N - 1))
# def rob(nums):
#     flag = [0 for i in range(len(nums) + 2)]
#     for i in range(len(nums)):
#         flag[i + 2] = max(flag[i] + nums[i], flag[i + 1])
#     r=0
#     for i in range(len(nums)-1,-1,-1):
#         if flag[i + 2]-flag[i]==nums[i] and nums[i]!=0:
#             r+=1
#     return flag[-1],max(r-1,0)
# v1,v2=rob(values)
v1,v2=func(values,N)
print(v1,v2)
