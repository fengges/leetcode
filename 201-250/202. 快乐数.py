class Solution:
    def isHappy(self, n):
        # 如果是快乐数 最后的结果一定会计算到1
        # 不是快乐数最后一定会有循环，比如 2-4-16-37-58-89-145-42-20-4
        # 我们用字典记录出现过的数字
        dic={}
        # 等于1的时候，是快乐数，结束循环
        while n!=1:
            #如果n在字典里面，则出现了循环，则这个数就不是快乐数
            print(n)
            if n in dic:
                return False
            # 将n加入字典
            dic[n]=1
            # 计算各个位数的平方和 例  145   n=1*1+4*4+5*5
            # 数字变字符串，主要是为了取每一位数方便，其实还有其他方法
            s=str(n)
            n=0
            for i in s:
                # 计算的时候要变成int哈
                n+=int(i)*int(i)
        return True
s=Solution()

test=[
{"input":19,"output":True},
{"input":1,"output":True},

]


for t in test:
    r=s.isHappy(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
