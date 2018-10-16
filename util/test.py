import numpy as np
import pandas as pd
import xlrd
#零均值化
def zeromean(datamat):
    meanval=np.mean(datamat, axis=0)     #按列求均值，即求各个特征的均值
    newdata=datamat-meanval             #每个数减去均值
    return newdata, meanval


def pca(datamat, n):
    newdata, meanval = zeromean(datamat)           #调用函数求均值
    covmat = np.cov(newdata, rowvar=0)    #求协方差矩阵,若rowvar非0，一列代表一个样本，为0，一行代表一个样本
    eigvals, eigvects = np.linalg.eig(np.mat(covmat))#求特征值和特征向量,特征向量是按列放的，即一列代表一个特征向量,mat转化为矩阵，eig是求特征值和特征向量
    eigvalindice = np.argsort(eigvals)            #对特征值从小到大排序
    n_eigvalindice = eigvalindice[-1:-(n+1):-1]   #最大的n个特征值的下标,逆序遍历
    n_eigvect = eigvects[:, n_eigvalindice]        #最大的n个特征值对应的特征向量，
    lowddatamat = newdata*n_eigvect               #低维特征空间的数据，均值化的数据乘以它的特征向量,第一列为样本数据和第一主成分的乘积
    reconmat = (lowddatamat*n_eigvect.T)+meanval  #重构数据，返回原样了
    return lowddatamat, reconmat


def percentage2n(eigvals, percentage):
    sortarray =  np.sort(eigvals)   #升序
    sortarray = sortarray[-1::-1]  #逆转，即降序
    arraysum = sum(sortarray)#计算累计贡献率
    tmpsum = 0
    num = 0
    for i in sortarray:
        tmpsum += i#挨个增加
        num += 1#遍历循环
        if tmpsum >= arraysum*percentage:
            return num


def excel_to_matrix(path):
    table = xlrd.open_workbook(path).sheets()[0]  # 获取第一个sheet表
    row = table.nrows-2 # 行数
    col = table.ncols  # 列数
    datamatrix = np.zeros((row, col))  # 生成一个nrows行ncols列，且元素均为0的初始矩阵
    for x in range(col):
        cols = table.col_values(x) # 把list转换为矩阵进行矩阵操作
        try:
            datamatrix[:, x] = cols[1:-1]  # 按列把数据存进矩阵中
        except:
            datamatrix[:, x]=[0 for i in range(row)]
    return datamatrix



if __name__=="__main__":
    datafile = r'testdata.xlsx'
    datamatrix=excel_to_matrix(datafile)
    print(datamatrix)
    new, old=pca(datamatrix,20)
    # print('降维之后的矩阵:')
    # print(new)
    # print('重构之后的矩阵：')
    # print(old)
