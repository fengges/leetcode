import sys
line= sys.stdin.readline().strip()
K=int(line)
line= sys.stdin.readline().strip()



def func( s, k):
    ans, start, count, nums = 0, 0, 0, [0 for _ in range(256)]
    for i, char in enumerate(s):
        if nums[ord(char)] == 0:
            count += 1
        nums[ord(char)] += 1

        while count > k:
            nums[ord(s[start])] -= 1
            if nums[ord(s[start])] == 0:
                count -= 1
            start += 1

        ans = max(ans, i - start + 1)
    return ans

tmp=func(line,K)
print(tmp)