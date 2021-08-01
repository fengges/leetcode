# import sys
# line= sys.stdin.readline().strip()
# n=int(line)
# line= sys.stdin.readline().strip()
# arr=set(map(int,line.split(' ')))
#
# result=0
# for a in arr:
#     result^=a
# # 应当优化到一层循环   (i%n)^(j%n)  怎么化简
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         result^=i%j
# print(result)
def test():
    for i in range(1,100):
        # print(i)
        for j in range(1,100):
            for k in range(1,100):
                # if i^j^k !=k^j^i:
                #     print(i^j^k ,k^j^i)
                #     print(i, j, k)
                if (i^j)%k!=((i%k)^(j%k))%k:
                    print(i,j,k)
                    print((i^j)%k,((i%k)^(j%k))%k)
test()