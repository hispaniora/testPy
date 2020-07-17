import sys
import xlrd


xlsBook = xlrd.open_workbook(r'F:\testData\GDAPIs1.xls')  # 以只读的方式打开xlsx文件
xlsSheet = xlsBook.sheets()[0]  # 获取Excel第一个sheet中的数据
rowCount = xlsSheet.nrows  # 获取sheet的行数
print(str(rowCount))
