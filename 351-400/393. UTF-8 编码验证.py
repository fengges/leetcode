class Solution:
    def validUtf8(self, data):
        cnt = 0  # 用于记录当前是几字节编码
        for byte in data:
            if 128 <= byte <= 191:  # 表示这数字对应的2进制 为 10xxxxxx 类型的，所以不能作为开头
                if cnt == 0:  # 此时，如果 cnt==0 直接返回 False
                    return False
                cnt -= 1  # 当前 位 合法，进入下一位比较
            else:  # -- -- 判断 当前 二进制 非10 开头的情况
                if cnt:
                    return False
                if byte < 128:  # 表示一个字节的情况
                    continue
                elif byte < 224:  # 两个字节的情况
                    cnt = 1
                elif byte < 240:  # 三个字节的情况
                    cnt = 2
                elif byte < 248:  # 四个字节的情况
                    cnt = 3
                else:  # 其他情况均为 False
                    return False
        return cnt == 0  # 比较结束， cnt 必须为0 才是合法的

s=Solution()
test=[
{"input":[197,197,1], "output":True},

]

for t in test:
    r=s.validUtf8(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))