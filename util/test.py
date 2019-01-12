from collections import Counter

test="吴静，周律，田金平，张晓健，石磊，王慧，张芳，李广贺，梁鹏，杜鹏飞，何苗，周小红，陈吕军，王毅，汪诚文，文湘华，杨云锋，黄俊，王玉珏，左剑恶，王凯军"
test=test.split("，")
c=Counter(test)
all=[k for k in c if c[k]>1]
print(all)