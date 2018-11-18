import numpy as np
fr = open('testdata8.xls', 'rb')
arrayOLines = fr.readlines()  # 按行读取,这个时候的arrayolines是一个表格,但是显示的不是数
numberOfLines = len(arrayOLines)  # 统计数据集行数（样本个数）
attribute_num=3
dataMat = np.zeros((numberOfLines, attribute_num))  # 初始化一个0矩阵，行数为样本数，列数为attribute_num,这个数是给定的
classLabelVector = []  # 分类标签，定义一个矩阵,表示最后一列的信息
index = 0
for line in arrayOLines:  # 对于每一行
    line = line.strip()  # strip() 删除字符串头尾的空格或换行符
    listFromLine = line.strip().split()  # 将一个字符串分割，不带参数时以空格进行分割，当代参数时，以该参数进行分割,返回的是分割后的字符串列表，此时是将每一行的数据进行分割
    dataMat[index, :] = listFromLine[
                        0:attribute_num]  # dataMat[index, : ]的意思是第一行的所有值，因为index这个时候为0，表示第一行，读取数据对象属性值，每一行的数据都读出来
    classLabelVector.append(listFromLine[-1])  # 读取分类信息，应该是获取每一行的最后一个数据？
    index += 1
    # 这个循环下来应该是获取了文件里的所有数据
dataSet = []  # 数组转化成列表
index = 0
for index in range(0, numberOfLines):  # 对于每一行
    temp = list(dataMat[index, :])  # 把每一行的数据储存在列表里
    temp.append(classLabelVector[index])  # 然后每一行还要增加原始的最后一列的数据？
    dataSet.append(temp)  # 把每一行的数据加进去
