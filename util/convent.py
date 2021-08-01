import xlrd
import xlsxwriter

def main(input_name,name):

    newbook = xlsxwriter.Workbook(name+'.xlsx')
    newsheet=newbook.add_worksheet()

    cell_format1 = newbook.add_format({'align': 'center','valign':'vcenter','text_wrap':True,'bg_color':'#FCE4D6','border':1,'border_color':'#0D0D0D'})
    cell_format2 = newbook.add_format({'align': 'center','valign':'vcenter','text_wrap':True,'bg_color':'#DDEBF7','border':1,'border_color':'#0D0D0D'})
    newsheet.merge_range(0,0,1,1, name,cell_format1)

    type=[
        ["数学：W",[0,2,0,7]]	,
        ["看数学视频",[1,2]]	,
        ["做练习题",[1,3]]	,
        ["看复习全书",[1,4]]	,
        ["做真题",[1,5]]	,
        ["回顾错题",[1,6]]	,
        ["其他",[1,7]]	,
        ["数学学习时长小计", [0,8,1,8]],
        ["英语：X",[0,9,0,14]]	,
        ["看英语视频",[1,9]]	,
        ["背单词",[1,10]]	,
        ["练阅读",[1,11]]	,
        ["做真题",[1,12]]	,
        ["背/练作文",[1,13]]	,
        ["其他",[1,14]]	,
        ["英语学习时长小计",[0,15,1,15]]	,
        ["政治：Y",[0,16,0,21]]	,
        ["看政治视频",[1,16]]	,
        ["看精讲精练",[1,17]]	,
        ["做练习题",[1,18]]	,
        ["做真题",[1,19]]	,
        ["背知识点",[1,20]]	,
        ["其他",[1,21]]	,
        ["政治学习时长小计",[0,22,1,22]]	,
        ["专业课：Z",[0,23,0,28]]	,
        ["看专业课视频",[1,23]]	,
        ["看课本",[1,24]]	,
        ["做练习题",[1,25]]	,
        ["背知识点",[1,26]]	,
        ["做真题",[1,27]]	,
        ["其他",[1,28]]	,
        ["专业课学习时长小计",[0,29,1,29]],
        ["总学习时长",[0,30,1,30]]
    ]
    for t in type:
        # t=type[1]
        if len(t[1])==4:
            newsheet.merge_range(t[1][0],t[1][1],t[1][2],t[1][3], t[0],cell_format2)
        elif len(t[1])==2:
            newsheet.write(t[1][0], t[1][1], t[0], cell_format2)

    def getCol(data, tableid, index):
        # 通过文件名获得工作表,获取工作表1
        table = data.sheet_by_index(tableid)
        # print("{0} {1} {2}".format(table.name, table.nrows, table.ncols))
        tmp = [[table.cell(i, j).value for j in index] for i in range(table.nrows)]
        return tmp
    def getRow(data, tableid, index):
        # 通过文件名获得工作表,获取工作表1
        table = data.sheet_by_index(tableid)
        # print("{0} {1} {2}".format(table.name, table.nrows, table.ncols))
        tmp = [[table.cell(j, i).value for i in range(table.ncols) ] for j in index]
        return tmp

    data = xlrd.open_workbook(input_name)
    date=getCol(data,0,[0])


    start=2
    for i,d in enumerate(date):
        if i==0:
            continue
        t=d[0]

        newsheet.merge_range(start,0,start+2,0, t,cell_format1)
        newsheet.write(start, 1, '学习时长', cell_format1)
        newsheet.write(start+1, 1, '占科目比', cell_format1)
        newsheet.write(start+2, 1, '占总时长比', cell_format1)

        nums=getRow(data,0,[i])
        nums=nums[0]
        for i in range(4):
            nums.insert(21*i+20,'')
            nums.insert(21 * i + 20, '')
        for k,v in enumerate(nums):
            if k==0:
                continue
            n=(k-1)%3
            s=(k-1)//3+2
            if n==0:
                newsheet.write(start, s, v)
            elif n==1:
                newsheet.write(start + 1, s, v)
            else:
                newsheet.write(start + 2, s, v)
        start+=3
    newbook.close()
import sys

if __name__=="__main__":
    input_name=input('输入文件名：')
    name = input('输出文件名')

    main(input_name,name)






