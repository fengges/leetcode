class Solution:
    # def get_max_production_num(self,limit,plan):
    def purchase_items(self,num,price,discount,budget):
        left_num=num
        use_budget=0
        buy=[]
        # 加一天原价
        size=len(discount)
        if discount[0][0]==1:
            falg=True
            for i in range(size-1):
                if discount[i][0]+1<discount[i+1][0]:
                    discount.insert([discount[i][0]+1,price,num])
                    falg=False
            if falg:
                discount.append([discount[-1]+1,price,num])
        else:
            discount.insert(0,[1,price,num])

        for d in discount:
            if left_num<=d[2] and use_budget+d[1]*left_num<=budget:
                return d[0]
            # 买入
            tmp_num=min((budget-use_budget)//d[1],d[2])
            left_num-=tmp_num
            use_budget+=tmp_num*d[1]
            buy.extend([d[1]]*tmp_num)
            # 不够,去掉最贵的
            for i in range(d[1]-tmp_num):
                obj=max(buy)
                if obj<=d[1]:
                    break

                index=buy.index(obj)
                buy.pop(index)
                use_budget-=(obj-d[1])
                buy.append(d[1])
        return -1



s=Solution()

test=[
    {"input":[3,5,[[2,4,2],[3,1,4]],14],"output":2},
    {"input":[4,10,[[2,5,3],[3,6,2],[4,2,1],[6,1,4],[100,3,1]],18],"output":4},
    {"input":[2,4,[[2,3,3]],10],"output":1},
]
for t in test:
    r=s.purchase_items(*t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
    else:
        print("success:"+str(t['output'])+" out:"+str(r))

