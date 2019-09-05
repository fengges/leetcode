import sys
N= int(sys.stdin.readline().strip())

line = sys.stdin.readline().strip()
values=list(map(int, line.split()))

def func2(nums,n):
    if n == 0:
        return 0
    pre_sum = [nums[0]]
    for i in range(1, n):
        pre_sum.append(pre_sum[-1] + nums[i])

    index_stack = [0]
    max_multi = 0
    curindex = 1
    while curindex < n or (curindex == n and len(index_stack) > 0):
        if curindex < n and (len(index_stack) == 0 or nums[curindex] >= nums[index_stack[-1]]):
            index_stack.append(curindex)
            curindex += 1
        else:
            min_num = nums[index_stack.pop()]

            cursum = pre_sum[curindex-1] - (pre_sum[index_stack[-1]] if len(index_stack) > 0 else 0)
            curmax = min_num * cursum
            max_multi = max(max_multi, curmax)
    return max_multi
print(func2(values,N))
