x = [2,2.2,1.7,7,8,5,4]
y = [4,2.8,3.2,8,4,3,2]
txt = ['数据挖掘','刘玉葆','衣杨','颜海平','冯峰','何福胜','吕中舌']

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.scatter(x, y)
def func(plt,i,c):
    plt.annotate(txt[i], xy = (x[i], y[i]), xytext = (x[i]+0.1, y[i]+0.1),color=c) # 这里xy是需要标记的坐标，xytext是对应的标签坐标
func(plt,0,"r")
func(plt,1,"y")
func(plt,2,"y")
func(plt,3,"b")
func(plt,4,"b")
func(plt,5,"b")
func(plt,6,"b")
plt.show()