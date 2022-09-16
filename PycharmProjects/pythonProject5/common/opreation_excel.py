import xlrd
from xlrd import xldate_as_tuple
from datetime import datetime

class OperationExcel:
    def __init__(self, filepath):
        book = xlrd.open_workbook(filename=filepath)
        self.sheet = book.sheet_by_index(0)

    def read_excel(self):
        rows = self.sheet.nrows
        cols = self.sheet.ncols
        all_data_list = []
        for row in range(1, rows):
            data_list = []
            for col in range(cols):
                ctype = self.sheet.cell(row, col).ctype
                cell = self.sheet.cell_value(row, col)
                if ctype == 2 and cell % 1 == 0:
                    cell = int(cell)
                elif ctype == 3:
                    date = datetime(*xldate_as_tuple(cell, 0))
                    cell = date.strftime("%Y-%m-d %H-%M-%S")
                elif ctype == 4:
                    cell = True if cell == 1 else False  # 三目云算法
                data_list.append(cell)
            all_data_list.append(data_list)
        return all_data_list

    def get_data_by_dict(self):
        keys = self.sheet.row_values(0)
        values = self.read_excel()
        data_list = []
        for value in values:
            tmp = zip(keys, value)
            data_list.append(dict(tmp))
        return data_list


if __name__ == '__main__':
    oper = OperationExcel('testdata.xlsx')
    # data = oper.read_excel()
    data = oper.get_data_by_dict()
    print(data)
