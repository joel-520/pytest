import xlwt
#coding:utf_8
# excel  2007版之前创建的表格。xls结尾的，需要用xlwt模块导入
# Excel 2007版之后创建的表格是。xlsx结尾的，需要使用openpxyl模块倒入
# 创建工作博
wb = xlwt.Workbook(encoding='utf-8')
# 括号内参数为表名
ws = wb.add_sheet('职位需求分析表')
# 参数1：行数
# 参数2：列数 从0开始计数
# 参数3：值   即单元格的内容
ws.write(0, 0, label='序号')
ws.write(0, 1, label='职位')
ws.write(0, 2, label='意向城市')
ws.write(0, 3, label='薪资范围')

ws.write(1, 0, label='01')
ws.write(1, 1, label='python研发工程师')
ws.write(1, 2, label='北京')
ws.write(1, 3, label='30k-50k')

#设置表格宽度
import xlwt workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Sheet')
worksheet.write(0, 0,'My Cell Contents')
# 设置单元格宽度
worksheet.col(0).width = 3333
workbook.save('cell_width.xls')

#输入一个日期到单元格
import xlwt
import datetime
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Sheet')
style = xlwt.XFStyle()
style.num_format_str = 'M/D/YY' # Other options: D-MMM-YY, D-MMM, MMM-YY, h:mm, h:mm:ss, h:mm, h:mm:ss, M/D/YY h:mm, mm:ss, [h]:mm:ss, mm:ss.0
worksheet.write(0, 0, datetime.datetime.now(), style) workbook.save('Excel_Workbook.xls')

#向单元格输入一个公式
import xlwt workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Sheet')
worksheet.write(0, 0, 5) # Outputs 5
worksheet.write(0, 1, 2) # Outputs 2
worksheet.write(1, 0, xlwt.Formula('A1*B1')) # Should output "10" (A1[5] * A2[2]) worksheet.write(1, 1, xlwt.Formula('SUM(A1,B1)'))
workbook.save('Excel_Workbook.xls')

#向单元格里面添加一个单元格
import xlwt
workbook = xlwt.Workbook
worksheet = workbook/add_sheet('My Sheet')
worksheet.write(0,0,xlwt.Formula('HYPERLINK("http://www.googele.com";"Google")')) #0
workbook.save('Excel1_Workbook.xls')

#合并同列行
import xlwt workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Sheet')
worksheet.write_merge(0, 0, 0, 3, 'First Merge') # Merges row 0's columns 0 through 3. font = xlwt.Font() # Create Font
font.bold = True # Set font to Bold style = xlwt.XFStyle() # Create Style
style.font = font # Add Bold Font to Style
worksheet.write_merge(1, 2, 0, 3, 'Second Merge', style) # Merges row 1 through 2's columns 0 through 3.
workbook.save('Excel_Workbook.xls')

#设置单元格内其他对齐方式
import xlwt
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Sheet')
alignment = xlwt.Alignment() # Create Alignment
alignment.horz = xlwt.Alignment.HORZ_CENTER # May be: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
alignment.vert = xlwt.Alignment.VERT_CENTER # May be: VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED
style = xlwt.XFStyle() # Create
Style style.alignment = alignment # Add Alignment to Style
worksheet.write(0, 0, 'Cell Contents', style)
workbook.save('Excel_Workbook.xls')


#为单元格添加边框
import xlwt
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Sheet')
borders = xlwt.Borders() #  Create Borders
borders.left = xlwt.Borders.DASHED
     DASHED 虚线
     NO_Line 没有
     THIN 实线

# May be : NO_Line, THIN, MEDIUM, DASHED, DOTTED, THICK, DOUBLE, HATR, MEDIUM_DASHED,
borders.right = xlwt.Borders.DASHED
borders.top = xlwt.Borders.DASHED
borders.botton = xlwt.Borders.DASHED
borders.left_colour = 0x40
borders.right_colour =0x40
borders.top_colour = 0x40
borders.botton_colour = 0x40
style = xlwt.XFStyle()   # Create Style
style.borders = borders   # Add Borders to style
worksheet.write(0,0,'Cell Contents',style)
workbook.save('Excel_Workbook.xls')

#单元格的背景颜色
import xlwt
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Sheet')
pattern = xlwt.Pattern() # Create the pattern
pattern.pattern = xlwt.Pattern.SOLID_PATTEREN # Map be :
pattern.pattern_fore_colour = 5
style = xlwt.XFStyle()
style.pattern = pattern
worksheet.write(0,0,'Cell Contents',style)
workbook.save('Excel_Workbook.xls')


from urllib import request
import requests
import re
import json
import xlwt
list = []
dict={
    '1':'0',
    '2':'60',
    '3':'120',
    '4':'180',
    '5':'240'
}     #这里为爬去前5页的网站循环
#p =2
#for x in range(60,300,60)
#p +=1   观察规律之后可以用这种方法！其他方法都有1
for x,y in dict.items():
    url = 'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=60&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&lastUrlQuery=%7D%22p%22:{},%22jl%22:%22530%22,%22kw%22:%22python%22,%22kt%22:%223%22%7D'.format(y,x)
    req = requests.get(url,headers ={
        'User-Agent':"Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
    })
    pat = re.compile(r'.*?"company":.*?"url":.*?"name":(.*?)"size".*?"positionURL":.*?"salary"(.*?)"emplType"(.*?)"jobName":(.*?)"industry"',re.S)
    ree = re.findall(pat,req.text)
    list.append(ree)


wb = xlwt.Workbook(encoding='utf-8')
ws = wb.add_sheet('智联python招聘信息')
ws.write(0,0,label='序号')
ws.write(0,1,label='招聘公司')
ws.write(0,2,label='工资')
ws.write(0,3,label='职业')
ws.write(0,4,label='职位')
a= 1
for index in list:
    # print(index)
    for x in index:
        # print(x)
        ws.write(a,0,label=a)
        ws.write(a,1,label=x[0])
        ws.write(a,2,label=x[1])
        ws.write(a,3,label=x[2])
        ws.write(a,4,label=x[3])
        a +=1
ws.col(4).width = 15999
ws.col(1).width = 13999
wb.save('pipi.xls')
