#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 比较版本号
# @param version1 string字符串
# @param version2 string字符串
# @return int整型
#
class Solution:
    def compare(self , version1: str, version2: str) -> int:
        # write codeQ here
        ans1=version1.split('.')
        ans2=version2.split('.')
        while ans1[-1]=='0':
            ans1.pop()
        while ans2[-1]=='0':
            ans2.pop()
        size1,size2=len(ans1),len(ans2)
        size=min(size1,size2)

        for i in range(size):
            if int(ans1[i])==int(ans2[i]):
                continue
            elif int(ans1[i])>int(ans2[i]):
                return 1
            else:
                return -1
        if size1==size2:
            return 0
        elif size1>size2:
            return 1
        else:
            return -1