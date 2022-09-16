# -*- coding: utf-8 -*-
# @Time : 2022/7/19 10:09
# @Author : joel
# @Email : 770546904@qq.com
# @File : test_xld.py


import xlrd2


workbook = xlrd2.open_workbook(r"../cases/获取token.csv")
# sheet1 = workbook.sheets()[1]
# sheet2 = workbook.sheet_names()
# sheet3 = workbook.sheet_loaded(0)
# sheet4 = workbook.unload_sheet("Sheet2")
# sheet5 = workbook.sheet_by_index(2)
sheet6 = workbook.sheet_by_name("Sheet1")
#
#
#
# print(sheet1)
# print(sheet2)
# print(sheet3)
# print(sheet4)
# print(sheet5)
# print(sheet6)
#
row = sheet6.nrows
print("row: ",row)
#
col = sheet6.ncols
# print(col)
#
# # 返回该行的有效单元格长度
# num = sheet6.row_len(0)
# print(num)
#
# # rowx表示是获取第几行的数据
# # start_col表示从索引为多少开始，
# # end_colx表示从索引为多少结束，
# # end_colx为None表示结束没有限制
# # 获取指定行中的数据并以列表的形式返回
# sheet6_list = sheet6.row_values(rowx=0, start_colx=0, end_colx=None)
# print(sheet6_list)
#
# # colx表示是获取第几列的数据
# # start_rowx表示从索引为多少开始，end_rowx表示从索引为多少结束，
# # end_rowx为None表示结束没有限制
# # 获取指定列中的数据并以列表的形式返回
# sheet6_list = sheet6.col_values(colx=0, start_rowx=0, end_rowx=None)
# print(sheet6_list)
#
# # 获取指定单元格内的值
url_value = sheet6.cell_value(rowx=row+1, colx=4)
method_value = sheet6.cell_value(rowx=1, colx=1)
params_value = sheet6.cell_value(rowx=1, colx=1)
# print(value)
#
# value = sheet6.cell(rowx=1, colx=1)
# print(value)
#
#
# value = sheet6.cell_type(rowx=1, colx=1)
# print(value)



# 循环获取每行的数据
for row in range(row):
    for col in range(col):
        value = sheet6.cell_value(row, col)
        print('第{}行{}列的数据为：{}'.format(row, col, value))


