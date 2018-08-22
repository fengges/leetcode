class Solution:
    def thirdMax(self, num):
        # 例子1 [3, 2, 1]  例子2  [1, 2]  例子3  [2, 2, 3, 1]

        # 声明数组容器 c# 可以用 List<int> tmp =new List<int>();
        tmp=[]
        # 对nums数组遍历
        # foreach(var i in num) c#的写法
        for i in num:
            # 一个元素只加入一次，重复的元素会忽略
            # c# 我记得在数据统计的地方出现过一次 SJTJController 下面的tongji
            # if (tmp.indexOf(i)<0)
            # 判断是否出现过
            if i not in tmp:
                # c#写法 tmp.add(i)
                tmp.append(i)
        # 去掉重的元素之后 例子1 tmp=[3,2,1]     例子2  tmp=[1, 2]     例子3  [2, 3, 1]   例子3的重复元素没有了

        # 排序 tmp.Sort() c#的写法是首字母大写
        # 排序是 将 例子1 变成 tmp=[1,2,3]  例子2  tmp=[1,2]  例子3  tmp=[1，2，3]
        tmp.sort()
        # 倒序 tmp.Reverse() c#的写法是首字母大写
        # 将 例子1 变成 tmp=[3，2，1]  例子2  tmp=[2，1]  例子3  tmp=[3，2，1]
        # 这样 第一个数，就是第一大，第三个数，就是第三大
        tmp.reverse()
        # 判断长度是否小于3 小于3的话就是没有第三大是数，就是返回最大数
        # c# 写法 if (tmp.Count<3)
        if len(tmp)<3:
            return tmp[0]
        return tmp[2]

s=Solution()

test=[

{"input":[1,2],"output": 2},
{"input":[2,2,3,1],"output":1},
]
for t in test:
    r=s.thirdMax(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.thirdMax(t['input'])
