class Solution:
    def findLengthOfLCIS(self, nums):
        # 首先判断数组长度是0，如果是0，那么最长联系的当然是0
        # if (nums.Count==0)
        if len(nums)==0:
            return 0
        # maxL 是保存，最长连续递增的记录
        # L 是当前连续递增的记录
        # 默认值是1的原因   一个数也是算连续递增，比如  例子1 [2,1]  ， [2] 是连续递增,长度为1 ， [1] 也是连续递增,长度为1
        maxL=1
        L=1
        #   判断 次数应该是n-1 例子2  [1,3,5,4,7]  1和3 比较  3和5  5和4 4和7  比较次数是数组长度的少1 的
        # c#代码  for(int i=0;i<nums.Lenght-1;i++)
        for i in range(len(nums)-1):
            # 如果后面一个数比前面的大，则连续递增+1
            if nums[i+1]>nums[i]:
                L+=1
                #更新L的时候记得要更新maxL
                maxL=max(L,maxL)
            else:
                # 如何后面一个数小于等于前面一个数，连续递增就断了，就要更新L的值
                # 比如 例子2 [1,3,5,4,7]  i=2 的时候   nums[i+1]<nums[i]  5<4  4和前面的数不能构成连续递增，但是4自己就是也该连续递增
                # 所以这里的L 更新为1 ，我感觉这个题目最难理解的也是这个地方为什么更新为1
                L=1
        return maxL


s = Solution()
test = [
{"input": [1,3,5,4,7], "output": 3},
{"input": [2,2,2,2,2], "output": 1},

]

for t in test:
    r = s.findLengthOfLCIS(t['input'])
    if r != t['output']:
        print("error:" + str(t) + " out:" + str(r))
        r = s.findLengthOfLCIS(t['input'])