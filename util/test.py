import  itchat
import os
import csv
import pandas as pd
from pyecharts import Bar,Pie,Geo
import shutil  as sh

# 根据index打印朋友的信息
def print_Info(friends):
    UserName = friends['UserName']
    NickName = friends['NickName']
    HeadImgUrl = friends['HeadImgUrl']
    ContactFlag = friends['ContactFlag']
    MemberCount = friends['MemberCount']
    RemarkName = friends['RemarkName']
    Sex = friends['Sex']
    Province = friends['Province']
    City = friends['City']
    MemberCount=friends['MemberCount']
    Signature=friends['Signature']

    print('---------------UserInfo-------------')
    print("UserName:", UserName)
    print("NickName:", NickName)
    print("HeadImgUrl:", HeadImgUrl)
    print("ContactFlag:", ContactFlag)
    print("MemberCount:", MemberCount)
    print("RemarkName:", RemarkName)
    print("Sex:", Sex)
    print("Province:", Province)
    print("City:", City)
    print("MemberCount:", MemberCount)
    print("Signature:", Signature)
    print('---------------END-------------')

    return


# 统计打印男女的比例，并生成Pie.html
def paint_CountScan(friends,nickName,path):

    # 其中1为男，2为女
    male=female=other=0

    for i in friends[1:]:
        if i['Sex']==1:
            male+=1
        elif i['Sex']==2:
            female+=1
        else:
            other+=1

    total=len(friends[1:])

    maleScan='{:.2%}'.format(male/total)
    femaleScan='{:.2%}'.format(female/total)
    otherScan='{:.2%}'.format(other/total)

    print('---------------Scan-------------')
    print('total:',total,'\tmale:',male,'\tfemale:',female,'\tother:',other)
    print('maleScan:',maleScan)
    print('femaleScan:',femaleScan)
    print('otherScan:',otherScan)
    print('---------------END-------------')

    attr=['meal','female','other']
    # data=[maleScan,femaleScan,otherScan]
    data=[male,female,other]
    pie=Pie("%s的Wechat男女分布比例"%nickName,background_color="#fff")
    pie.add("Wechat",attr,data,is_label_show=True)
    pie.show_config()
    dir = r'%s\%s的Wechat男女分布比例.html' % (path, nickName)
    pie.render(dir)

    return dir

# 根据自己的nickName创建对应的用户文件夹
def createDir(filename):
    try:
        os.mkdir(filename)
        print(filename,'文件夹创建成功')
    except Exception as e:
        print(e)
        print(filename, '文件夹创建失败，可能已经存在该文件夹')
    return

# 数据清洗，提取需要的信息
def get_UseInfo(friends):
    # 读取信息
    data = pd.DataFrame(friends)
    userName = data['UserName']
    nickName = data['NickName']
    headImgUrl = data['HeadImgUrl']
    contactFlag = data['ContactFlag']
    memberCount = data['MemberCount']
    remarkName = data['RemarkName']
    sex = data['Sex']
    province = data['Province']
    city = data['City']
    signature = data['Signature']
    #

    # 生成信息csv
    info = {'userName': userName, 'nickName': nickName, 'remarkName': remarkName, 'sex': sex, 'province': province,
            'city': city, 'signature': signature}
    dataFrame = pd.DataFrame(info)
    return dataFrame

# dataFrame为提取后的信息格式，保存dataFrame信息
def save_FriendsCsvFile(dataFrame,fileName,path):
    # 存储信息csv
    dir=r'%s\%s的朋友信息表.csv'%(path,fileName)
    dataFrame.to_csv(dir,sep=',')
    return dir

# dataFrame为提取后的信息格式
# 统计所在城市的信息，并保存下来
def save_CountCityCsvFile(dataFrame,fileName,path):
    count = dataFrame['nickName'].groupby(dataFrame['city']).count()
    city=pd.DataFrame(count[1:])
    dir = r'%s\%s的朋友所在城市统计表.csv' % (path, fileName)
    city.to_csv(dir)
    return  dir

# 根据城市的信息CSV文件，画出Bar,Pie图
def paint_CountCityCsvFile(cityPath,nickName,path):
    file = open(cityPath, 'r', encoding='utf-8')
    # 使用csv.reader读取csvfile中的文件
    csvFile=csv.reader(file)
    # 读取第一行每一列的标题
    header=next(csvFile)
    # 将csv 文件中的数据保存到data中
    city=[]
    count=[]
    for i in file:
        temp=i.split(',')
        city.append(temp[0])
        count.append(temp[1])

    # 画图
    # 柱状图
    bar = Bar("%s的朋友城市分布表" % nickName, "Data from WeChart", background_color="#fff",width=1600,height=600)
    bar.add("City", city, count,xaxis_label_textsize=12,xaxis_rotate=30)
    bar.show_config()
    dir_Bar = r'%s\%s的朋友城市分布表Bar.html' % (path, nickName)
    bar.render(dir_Bar)

    # 饼状图
    pie=Pie("%s的朋友城市分布表" % nickName, "Data from WeChart", background_color="#fff",width=1500,height=800,title_top=80,title_text_size=20)
    pie.add("City", city, count,  is_label_show=True,radius=[0,60])
    pie.show_config()
    dir_Pie = r'%s\%s的朋友城市分布表Pie.html' % (path, nickName)
    pie.render(dir_Pie)

    dir=[dir_Bar,dir_Pie]
    return dir

def copyPKL(nickName):
    list=os.listdir()
    for i in list:
        if i=='itchat.pkl':
            try:
                sh.copyfile('itchat.pkl',r'.\%s\itchat.pkl'%nickName)
            except Exception as e:
                print('%s文件夹不存在'%nickName)
    return

def add_ReplaceDir(dir,dirData):
    defType=[type('str'),type(['str','str'])]
    if type(dir)== defType[0]:
        dirData.append(dir)
    elif type(dir)==defType[1]:
        for i in dir:
            dirData.append(i)
    else:
        print(dir,'的类型是',type(dir),'不是指定的类型',defType[0],defType[1])
    return dirData

#根据提供的路径替换指定HTML中的标题
def replace_Title(filePath):
    content = []
    try:
        for file in filePath:
            title=file.split('\\')[-1].split('.')[0]
            with open(file, 'r', encoding='Utf-8') as f:
                content = f.readlines()
            f.close()

            content[4] = '    <title>%s</title>\n' % title
            # for i in range(0,5,1):
            #     print(content[i])

            f = open(file, 'w', encoding='utf-8')
            for j in content:
                f.write(j)
            f.close()

    except Exception as  e:
        print(filePath,'不存在')

    return

if __name__=="__main__":
    # 登录
    itchat.auto_login(hotReload=True)
    friends=itchat.get_friends(update=True)
    # 打印自己的信息
    user=friends[0]
    print_Info(user)

    # 创建用户文件夹
    nickName=user['NickName']
    createDir(nickName)
    copyPKL(nickName)
    path='.\%s'%nickName

    # 获取想要的数据
    friends = itchat.get_friends(update=True)
    data=get_UseInfo(friends)

    #要替换得title的HTML文件
    reHtmlDir=[]

    # 画出男女比例图
    print('----------------画出男女比例图------------')
    dir=paint_CountScan(friends, nickName, path)
    reHtmlPath=add_ReplaceDir(dir,reHtmlDir)
    print('----------------END------------')


    # 画出城市统计图
    print('----------------画出男女比例图------------')
    dir=save_FriendsCsvFile(data,nickName,path)
    cityFilePath=save_CountCityCsvFile(data,nickName,path)
    dir=paint_CountCityCsvFile(cityFilePath,nickName,path)
    reHtmlPath = add_ReplaceDir(dir, reHtmlDir)
    print('----------------END------------')

    # 替换标题
    print(reHtmlDir)
    replace_Title(reHtmlPath)